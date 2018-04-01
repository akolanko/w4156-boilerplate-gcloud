import logging
from flask import render_template, flash, redirect, url_for, session, jsonify
from app import app, db
from app.forms import *
from flask_login import current_user, login_user
from app.models import *
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.friends import are_friends_or_pending, get_friends, find_friend
from app.notifications import get_notifications, get_notification
from app.messages import *
from app.discover import discover_friends, search_interests, get_interests
from sqlalchemy import asc
from app.accounts import validate_account, calculate_age
from app.events import create_event, user_event_exists, get_recent_events, get_event_invitation


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('discover'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('discover')
        session["current_user"] = {
            "username": user.username,
            "id": user.id
        }
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    del session["current_user"]
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=(form.username.data).lower(), email=form.email.data, fname=form.fname.data, lname=form.lname.data, birthday=form.birthday.data)
        user.set_password(form.password.data)
        db.session.add(user)
        profile = Profile()
        db.session.add(profile)
        user.profile = profile
        db.session.commit()
        session["current_user"] = {
            "username": user.username,
            "id": user.id
        }
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<user_id>')
@login_required
def user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    profile = user.profile
    total_friends = len(get_friends(user.id))
    friends = get_friends(user.id)
    limited_friends = friends[:6]
    age = calculate_age(user.birthday)

    notifications = get_notifications(current_user.id)
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id)

    conversation = conversation_exists(user.id, current_user.id)
    return render_template('profile.html', user=user, profile=profile, total_friends=total_friends, are_friends=are_friends, is_pending_sent=is_pending_sent, is_pending_recieved=is_pending_recieved, friends=friends, notifications=notifications, limited_friends=limited_friends, conversation=conversation, age=age)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    # enable editing
    user = current_user
    profile = user.profile

    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        notifications = get_notifications(current_user.username)
        current_user.profile.about = form.about.data
        current_user.profile.meet = form.meet.data
        current_user.profile.skills = form.skills.data
        current_user.profile.location = form.location.data
        current_user.profile.work = form.work.data
        current_user.profile.interests = form.interests.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        notifications = get_notifications(form.username.data)
        form.about.data = current_user.profile.about
        form.meet.data = current_user.profile.meet
        form.skills.data = current_user.profile.skills
        form.location.data = current_user.profile.location
        form.work.data = current_user.profile.work
        form.interests.data = current_user.profile.interests

    return render_template('edit_profile.html', title='Edit Profile', user=user, profile=profile, notifications=notifications, form=form)


@app.route("/friends/<user_id>")
@login_required
def friends(user_id):
    """Show all friends"""
    user = User.query.filter_by(id=user_id).first_or_404()
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id)
    friends = get_friends(user_id)
    limited_friends = friends[:6]
    total_friends = len(friends)
    notifications = get_notifications(current_user.id)
    conversation = conversation_exists(user.id, current_user.id)
    age = calculate_age(user.birthday)
    return render_template("friends.html", user=user, friends=friends, total_friends=total_friends, are_friends=are_friends, is_pending_sent=is_pending_sent, is_pending_recieved=is_pending_recieved, notifications=notifications, limited_friends=limited_friends, conversation=conversation, age=age)


@app.route("/add_friend/", methods=["POST"])
def add_friend():
    """Send a friend request to another user"""
    user_id_2 = request.form.get("user_id_2")
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id_2)

    if current_user.id == user_id_2:
        return "You cannot add yourself as a friend."
    elif are_friends:
        return "You are already friends."
    elif is_pending_sent:
        return "Your friend request is pending."
    elif is_pending_recieved:
        return "You have already recieved a request from this user."
    else:
        friend_request = Friends(user_id_1=current_user.id, user_id_2=user_id_2, status=FriendStatus.requested)
        db.session.add(friend_request)
        db.session.commit()
        return "Request sent."


@app.route("/accept_friend/", methods=["POST"])
def accept_friend():
    """Accept a friend request from another user"""
    user_id_2 = request.form.get("user_id_2")
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id_2)

    if current_user.id == user_id_2:
        return "You cannot add yourself as a friend."
    elif are_friends:
        return "You are already friends."
    elif is_pending_recieved:
        friend_request = Friends.query.filter_by(user_id_1=user_id_2, user_id_2=current_user.id, status=FriendStatus.requested).first()
        friend_request.status = FriendStatus.accepted
        db.session.commit()
        return "Request accepted."
    else:
        return "An error occured."


@app.route("/unfriend/", methods=["POST"])
def unfriend():
    """Unfriend another user"""
    user_id_2 = request.form.get("friend_id")
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id_2)

    if are_friends:
        relationship = Friends.query.filter_by(user_id_1=current_user.id, user_id_2=user_id_2, status=FriendStatus.accepted).first()
        if relationship is None:
            relationship = Friends.query.filter_by(user_id_1=user_id_2, user_id_2=current_user.id, status=FriendStatus.accepted).first()
        db.session.delete(relationship)
        db.session.commit()
        return "Unfriend"
    else:
        return "You cannot unfriend this user."


@app.route("/delete_friend_request/", methods=["POST"])
def delete_friend_request():
    """Delete a friend request from another user"""
    user_id_2 = request.form.get("user_id_2")
    are_friends, is_pending_sent, is_pending_recieved = are_friends_or_pending(current_user.id, user_id_2)

    if is_pending_recieved:
        relationship = Friends.query.filter_by(user_id_1=user_id_2, user_id_2=current_user.id, status=FriendStatus.requested).first()
        db.session.delete(relationship)
        db.session.commit()
        return "Request removed."
    else:
        return "You cannot remove this request."


@app.route("/conversation/<id>", methods=['GET', "POST"])
@login_required
def conversation(id):
    conversation = Conversation.query.filter_by(id=id).first_or_404()

    if current_user.id == conversation.user_id_1:
        user_2 = User.query.filter_by(id=conversation.user_id_2).first()
    elif current_user.id == conversation.user_id_2:
        user_2 = User.query.filter_by(id=conversation.user_id_1).first()
    else:
        return redirect(url_for('home'))

    update_read_messages(conversation.id, user_2.id)
    notifications = get_notifications(current_user.id)
    messages = conversation.messages.order_by(asc(Message.timestamp)).all()
    conversations = get_conversations(current_user.id)
    eventform = NewEventForm()
    return render_template("messenger.html", conversation=conversation, user_2=user_2, conversations=conversations, messages=messages, notifications=notifications, eventform=eventform)


@app.route("/new_message/", methods=["POST"])
def new_message():
    conversation_id = request.form.get("conversation_id")
    body = request.form.get("body")
    message = Message(sender=current_user.id, conversation_id=conversation_id, body=body)
    db.session.add(message)
    db.session.commit()
    return "Message sent"


@app.route("/new_conversation")
@login_required
def new_conversation():
    notifications = get_notifications(current_user.id)
    conversations = get_conversations(current_user.id)
    return render_template("new_conversation.html", conversations=conversations, notifications=notifications)


@app.route("/create_conversation/<user_id>", methods=['GET', "POST"])
def create_conversation(user_id):
    conversation_id = build_conversation(current_user.id, user_id)
    if conversation_id:
        return redirect(url_for('conversation', id=conversation_id))
    else:
        return "An error occurred."


@app.route("/create_new_conversation/", methods=["POST"])
def create_new_conversation():
    username = request.form.get("username")
    user_2 = find_friend(username)
    if user_2 is None:
        return "Your search did not return any results."
    conversation = conversation_exists(current_user.id, user_2.id)
    if conversation:
        messages = conversation.messages
        return jsonify([conversation.serialize(), user_2.serialize(), [m.serialize() for m in messages], current_user.serialize()])
    else:
        c_id = build_conversation(current_user.id, user_2.id)
        if c_id:
            return jsonify([(get_conversation(c_id)).serialize(), user_2.serialize()])
        else:
            return "An error occurred."


@app.route("/new_event/<user_id>/", methods=["POST"])
def new_event(user_id):
    eventform = NewEventForm()
    if eventform.validate_on_submit():
        event = Event(title=eventform.title.data, date=eventform .date.data, start_time=eventform.start_time.data, end_time=eventform.end_time.data, location=eventform.location.data, notes=eventform.notes.data)
        db.session.add(event)
        create_event(event, current_user, user_id)
        return jsonify("Event Created.")
    return jsonify(eventform.errors)


@app.route("/discover")
@login_required
def discover():
    notifications = get_notifications(current_user.id)
    users_interests = discover_friends(current_user.id)
    return render_template("discover.html", notifications=notifications, users_interests=users_interests)


@app.route("/search_discover/", methods=["POST"])
def search_discover():
    interest = request.form.get("interest")
    users = search_interests(interest, current_user.id)
    if len(users) == 0:
        return "Your search did not return any results."
    else:
        return jsonify([[u.serialize(), [i.serialize() for i in get_interests(u.id)]] for u in users])


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    notifications = get_notifications(current_user.id)
    accform = UpdateAccountForm()
    pswform = UpdatePasswordForm()
    return render_template("account.html", notifications=notifications, user=current_user, pswform=pswform, accform=accform)


@app.route("/update_account/", methods=['POST'])
@login_required
def update_account():
    accform = UpdateAccountForm()
    if accform.validate_on_submit():
        current_user.fname = accform.fname.data
        current_user.lname = accform.lname.data

        found_err, username_err, email_err = validate_account(current_user, accform.username.data, accform.email.data)
        if found_err is True:
            return jsonify(["error", accform.errors, {"username": username_err, "email": email_err}])

        current_user.username = accform.username.data
        current_user.email = accform.email.data
        current_user.birthday = accform.birthday.data

        db.session.add(current_user)
        db.session.commit()
        return jsonify(["success", {"fname": accform.fname.data, "lname": accform.lname.data, "username": accform.username.data, "email": accform.email.data, "birthday": accform.birthday.data}])
    return jsonify(["error", accform.errors, False])


@app.route("/update_password/", methods=['POST'])
@login_required
def update_password():
    pswform = UpdatePasswordForm()
    if pswform.validate_on_submit():
        current_user.set_password(pswform.password.data)
        db.session.add(current_user)
        db.session.commit()
        return jsonify("Password updated.")
    return jsonify(pswform.errors)


@app.route("/delete_account/", methods=['POST'])
@login_required
def delete_account():
    db.session.delete(current_user)
    db.session.commit()
    return redirect(url_for('login'))


@app.route("/view_notification/", methods=['POST'])
@login_required
def view_notification():
    notification_id = request.form.get("notification_id")
    notification = get_notification(notification_id)
    db.session.delete(notification)
    db.session.commit()
    return "Notification deleted."


@app.route("/event/<event_id>")
@login_required
def event(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()
    user_event = user_event_exists(current_user.id, event.id)
    if user_event is None:
        return redirect(url_for('discover'))
    notifications = get_notifications(current_user.id)
    coming_up = get_recent_events(current_user.id)
    length = len(event.user_events)
    sent_invitation, received_invitation = get_event_invitation(event_id, current_user.id)
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return render_template('event.html', notifications=notifications, event=event, coming_up=coming_up, user_event=user_event, length=length, sent_invitation=sent_invitation, received_invitation=received_invitation, weekdays=weekdays)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
