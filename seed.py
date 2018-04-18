from app.models import *
import datetime


def example_data():
    karen = User(username='karen', email='karen@example.com', fname='Karen', lname='Smith', birthday=datetime.date(1990, 1, 1))
    karen.set_password('karen')
    dale = User(username='dale', email='dale@example.com', fname='Dale', lname='Sue', birthday=datetime.date(1998, 5, 10))
    dale.set_password('dale')
    matt = User(username='matt', email='matt@example.com', fname='Matt', lname='Anderson', birthday=datetime.date(2000, 8, 13))
    matt.set_password('matt')
    jake = User(username='jake', email='jake@example.com', fname='Jake', lname='Brown', birthday=datetime.date(1995, 12, 12))
    jake.set_password('jake')
    ellen = User(username='ellen', email='ellen@example.com', fname='Ellen', lname='James', birthday=datetime.date(2000, 4, 7))
    ellen.set_password('ellen')
    katie = User(username='katie', email='katie@example.com', fname='Katie', lname='Wolf', birthday=datetime.date(1992, 11, 22))
    katie.set_password('katie')
    dan = User(username='dan', email='dan@example.com', fname='Dan', lname='Kay', birthday=datetime.date(2002, 8, 4))
    dan.set_password('dan')
    dan2 = User(username='dan2', email='dan2@example.com', fname='Dan', lname='Smith', birthday=datetime.date(2000, 10, 9))
    dan2.set_password('dan2')
    dan3 = User(username='dan3', email='dan3@example.com', fname='Dan', lname='Allen', birthday=datetime.date(1995, 04, 12))
    dan3.set_password('dan3')

    friendship1 = Friends(user_id_1=1, user_id_2=2, status=FriendStatus.accepted)
    friendship2 = Friends(user_id_1=3, user_id_2=4, status=FriendStatus.requested)
    friendship3 = Friends(user_id_1=5, user_id_2=7, status=FriendStatus.accepted)
    friendship4 = Friends(user_id_1=6, user_id_2=5, status=FriendStatus.accepted)
    friendship5 = Friends(user_id_1=6, user_id_2=7, status=FriendStatus.accepted)
    friendship6 = Friends(user_id_1=2, user_id_2=6, status=FriendStatus.accepted)
    friendship7 = Friends(user_id_1=9, user_id_2=2, status=FriendStatus.accepted)
    friendship8 = Friends(user_id_1=2, user_id_2=8, status=FriendStatus.accepted)

    conversation1 = Conversation(user_id_1=1, user_id_2=2)
    conversation2 = Conversation(user_id_1=4, user_id_2=1)
    message1 = Message(sender=1, conversation_id=1, body='hello', read=True, timestamp=datetime.datetime(2017, 02, 22, 19, 53, 42))
    message2 = Message(sender=2, conversation_id=1, body='hey')
    message3 = Message(sender=2, conversation_id=1, body='how are you?')

    interest1 = Interest(name='running')
    interest2 = Interest(name='tennis')
    interest3 = Interest(name='biking')
    interest4 = Interest(name='hiking')
    user_interest1 = User_Interest(user_id=1, interest_id=1)
    user_interest2 = User_Interest(user_id=1, interest_id=2)
    user_interest3 = User_Interest(user_id=1, interest_id=3)
    user_interest4 = User_Interest(user_id=3, interest_id=2)
    user_interest5 = User_Interest(user_id=3, interest_id=4)
    user_interest6 = User_Interest(user_id=3, interest_id=1)
    user_interest7 = User_Interest(user_id=2, interest_id=1)
    user_interest8 = User_Interest(user_id=4, interest_id=2)
    user_interest9 = User_Interest(user_id=5, interest_id=1)
    user_interest10 = User_Interest(user_id=5, interest_id=2)
    user_interest11 = User_Interest(user_id=6, interest_id=1)
    user_interest12 = User_Interest(user_id=7, interest_id=3)

    event1 = Event(date=datetime.date(2018, 4, 30), start_time=datetime.time(20, 15), end_time=datetime.time(11, 15), title='Event 1', location='Campus', notes='Lorem ipsum')
    event2 = Event(date=datetime.date(2018, 4, 8), start_time=datetime.time(14, 30), end_time=datetime.time(15, 30), title='Event 2', location='Dodge')
    event3 = Event(date=datetime.date(2018, 4, 20), start_time=datetime.time(16, 00), end_time=datetime.time(18, 00), title='Event 3')
    event4 = Event(date=datetime.date(2018, 4, 18), start_time=datetime.time(9, 00), end_time=datetime.time(11, 30), title='Event 4')

    user_event1 = UserEvent(user_id=1, event_id=1, accepted=1)
    user_event2 = UserEvent(user_id=2, event_id=1, accepted=0)
    user_event3 = UserEvent(user_id=2, event_id=2, accepted=1)
    user_event4 = UserEvent(user_id=1, event_id=2, accepted=0)
    user_event5 = UserEvent(user_id=1, event_id=3, accepted=1)
    user_event6 = UserEvent(user_id=2, event_id=3, accepted=0)
    user_event7 = UserEvent(user_id=4, event_id=3, accepted=1)
    user_event8 = UserEvent(user_id=1, event_id=4, accepted=1)
    user_event9 = UserEvent(user_id=2, event_id=4, accepted=1)
    user_event10 = UserEvent(user_id=3, event_id=4, accepted=0)
    user_event11 = UserEvent(user_id=4, event_id=4, accepted=1)

    event_invite1 = EventInvitation(sender_id=1, receiver_id=2, event_id=1)
    event_invite2 = EventInvitation(sender_id=2, receiver_id=1, event_id=2)
    event_invite3 = EventInvitation(sender_id=1, receiver_id=2, event_id=3)

    notification1 = Notification(body="New event invitation from Karen", receiver_id=2, event_id=1, type=NotificationType.event_invite)
    notification2 = Notification(body="New event invitation from Dale", receiver_id=1, event_id=2, type=NotificationType.event_invite)
    notification3 = Notification(body="New event invitation from Karen", receiver_id=2, event_id=3, type=NotificationType.event_invite)
    notification4 = Notification(body="Karen updated the details of your event - Event 4", receiver_id=2, event_id=4, type=NotificationType.event_update)

    db.session.add_all([karen, dale, matt, jake, ellen, katie, dan, dan2, dan3, friendship1, friendship2, friendship3, friendship4, friendship5, friendship6, friendship7, friendship8, conversation1, conversation2, message1, message2, message3, interest1, interest2, interest3, interest4, user_interest1, user_interest2, user_interest3, user_interest4, user_interest5, user_interest6, user_interest7, user_interest8, user_interest9, user_interest10, user_interest11, user_interest12, event1, event2, event3, event4, user_event1, user_event2, user_event3, user_event4, user_event5, user_event6, user_event7, user_event8, user_event9, user_event10, user_event11, event_invite1, event_invite2, event_invite3, notification1, notification2, notification3, notification4])
    db.session.commit()
