from app.models import *
import datetime


def example_data():
    #id=1
    karen = User(username='karen', email='karen@example.com', fname='Karen', lname='Smith', birthday=datetime.date(1990, 1, 1))
    karen.set_password('karen')
    #id=2
    dale = User(username='dale', email='dale@example.com', fname='Dale', lname='Sue', birthday=datetime.date(1998, 5, 10))
    dale.set_password('dale')
    #id=3
    matt = User(username='matt', email='matt@example.com', fname='Matt', lname='Anderson', birthday=datetime.date(2000, 8, 13))
    matt.set_password('matt')
    #id=4
    jake = User(username='jake', email='jake@example.com', fname='Jake', lname='Brown', birthday=datetime.date(1995, 12, 12))
    jake.set_password('jake')
    #id=5
    ellen = User(username='ellen', email='ellen@example.com', fname='Ellen', lname='James', birthday=datetime.date(2000, 4, 7))
    ellen.set_password('ellen')
    #id=6
    katie = User(username='katie', email='katie@example.com', fname='Katie', lname='Wolf', birthday=datetime.date(1992, 11, 22))
    katie.set_password('katie')
    #id=7
    dan = User(username='dan', email='dan@example.com', fname='Dan', lname='Kay', birthday=datetime.date(2002, 8, 4))
    dan.set_password('dan')
    #id=8
    dan2 = User(username='dan2', email='dan2@example.com', fname='Dan', lname='Smith', birthday=datetime.date(2000, 10, 9))
    dan2.set_password('dan2')
    #id=9
    dan3 = User(username='dan3', email='dan3@example.com', fname='Dan', lname='Allen', birthday=datetime.date(1995, 04, 12))
    dan3.set_password('dan3')
    #id=10
    brian = User(username='brian', email='brian@example.com', fname='Brian', lname='Jones', birthday=datetime.date(1994, 5, 20))
    brian.set_password('brian')
    #id=11
    sam = User(username='sam', email='sam@example.com', fname='Sam', lname='Forrest', birthday=datetime.date(1998, 12, 15))
    sam.set_password('sam')
    #id=12
    lisa = User(username='lisa', email='lisa@example.com', fname='Lisa', lname='Heart', birthday=datetime.date(1996, 2, 6))
    lisa.set_password('lisa')
    #id=13
    chris = User(username='chris', email='chis@example.com', fname='Chris', lname='Davis', birthday=datetime.date(1990, 8, 17))
    chris.set_password('chris')
    #id=14
    blaine = User(username='blaine', email='blaine@example.com', fname='Blaine', lname='Davis', birthday=datetime.date(1991, 3, 25))
    blaine.set_password('blaine')
    #id=15
    emma = User(username='emma', email='emma@example.com', fname='Emma', lname='Thomson', birthday=datetime.date(1993, 5, 15))
    emma.set_password('emma')
    #id=16
    dylan = User(username='dylan', email='dylan@example.com', fname='Dylan', lname='Parker', birthday=datetime.date(1993, 7, 3))
    dylan.set_password('dylan')

    profile_karen = Profile(user_id=1, about="Lorem ipsum dolor.", location="NYC", skills=2, work="Student")
    profile_dale = Profile(user_id=2, about="Phasellus in dui lobortis.", location="NYC", work="Student", meet="Condimentum sapien sed, imperdiet velit.", skills=1)
    profile_matt = Profile(user_id=3, about="Donec vitae nisi sit amet risus feugiat bibendum.", location="NYC", work="Student", meet="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse luctus eu lorem nec egestas.", skills=3)
    profile_jake = Profile(user_id=4)
    profile_ellen = Profile(user_id=5)
    profile_katie = Profile(user_id=6)
    profile_dan = Profile(user_id=7)
    profile_dan2 = Profile(user_id=8)
    profile_dan3 = Profile(user_id=9)
    profile_brian = Profile(user_id=10)
    profile_sam = Profile(user_id=11)
    profile_lisa = Profile(user_id=12)
    profile_chris = Profile(user_id=13)
    profile_blaine = Profile(user_id=14)
    profile_emma = Profile(user_id=15)
    profile_dylan = Profile(user_id=16)

    friendship1 = Friends(user_id_1=1, user_id_2=2, status=FriendStatus.accepted)
    friendship2 = Friends(user_id_1=3, user_id_2=4, status=FriendStatus.requested)
    friendship3 = Friends(user_id_1=5, user_id_2=6, status=FriendStatus.requested)
    friendship4 = Friends(user_id_1=7, user_id_2=5, status=FriendStatus.requested)
    friendship5 = Friends(user_id_1=6, user_id_2=8, status=FriendStatus.accepted)
    friendship6 = Friends(user_id_1=9, user_id_2=6, status=FriendStatus.accepted)
    friendship7 = Friends(user_id_1=15, user_id_2=12, status=FriendStatus.requested)
    friendship8 = Friends(user_id_1=15, user_id_2=13, status=FriendStatus.requested)
    friendship9 = Friends(user_id_1=14, user_id_2=15, status=FriendStatus.requested)
    friendship10 = Friends(user_id_1=16, user_id_2=15, status=FriendStatus.requested)
    friendship11 = Friends(user_id_1=13, user_id_2=16, status=FriendStatus.requested)
    friendship12 = Friends(user_id_1=14, user_id_2=13, status=FriendStatus.accepted)
    friendship13 = Friends(user_id_1=9, user_id_2=14, status=FriendStatus.accepted)
    friendship14 = Friends(user_id_1=5, user_id_2=9, status=FriendStatus.accepted)
    friendship15 = Friends(user_id_1=8, user_id_2=5, status=FriendStatus.accepted)
    friendship16 = Friends(user_id_1=8, user_id_2=7, status=FriendStatus.accepted)
    friendship17 = Friends(user_id_1=8, user_id_2=9, status=FriendStatus.accepted)

    conversation1 = Conversation(user_id_1=1, user_id_2=2)
    conversation2 = Conversation(user_id_1=4, user_id_2=1)
    conversation3 = Conversation(user_id_1=8, user_id_2=5)
    conversation4 = Conversation(user_id_1=7, user_id_2=8)
    conversation5 = Conversation(user_id_1=8, user_id_2=9)
    conversation6 = Conversation(user_id_1=8, user_id_2=12)
    message1 = Message(sender=1, conversation_id=1, body='hello', read=True)
    message2 = Message(sender=2, conversation_id=1, body='hey')
    message3 = Message(sender=2, conversation_id=1, body='how are you?')
    message4 = Message(sender=8, conversation_id=3, body='hi', read=True)
    message5 = Message(sender=8, conversation_id=4, body='how is it going?', read=True)
    message6 = Message(sender=5, conversation_id=3, body='hi dan')
    message7 = Message(sender=7, conversation_id=4, body='good')
    message8 = Message(sender=5, conversation_id=3, body="what's up?")
    message9 = Message(sender=7, conversation_id=4, body='and yourself?')
    message10 = Message(sender=9, conversation_id=5, body='hello', read=True)

    interest1 = Interest(name='running')
    interest2 = Interest(name='tennis')
    interest3 = Interest(name='biking')
    interest4 = Interest(name='hiking')
    interest5 = Interest(name='soccer')
    interest6 = Interest(name='squash')
    interest7 = Interest(name='lifting')
    user_interest1 = User_Interest(user_id=1, interest_id=1)
    user_interest2 = User_Interest(user_id=1, interest_id=2)
    user_interest3 = User_Interest(user_id=1, interest_id=3)
    user_interest4 = User_Interest(user_id=3, interest_id=1)
    user_interest5 = User_Interest(user_id=3, interest_id=2)
    user_interest6 = User_Interest(user_id=3, interest_id=4)
    user_interest7 = User_Interest(user_id=2, interest_id=1)
    user_interest8 = User_Interest(user_id=5, interest_id=1)
    user_interest9 = User_Interest(user_id=6, interest_id=1)
    user_interest10 = User_Interest(user_id=4, interest_id=3)
    user_interest11 = User_Interest(user_id=15, interest_id=5)
    user_interest12 = User_Interest(user_id=15, interest_id=6)
    user_interest13 = User_Interest(user_id=16, interest_id=5)
    user_interest14 = User_Interest(user_id=12, interest_id=5)
    user_interest15 = User_Interest(user_id=7, interest_id=5)
    user_interest16 = User_Interest(user_id=7, interest_id=3)
    user_interest17 = User_Interest(user_id=8, interest_id=6)
    user_interest18 = User_Interest(user_id=8, interest_id=5)

    event1 = Event(date=datetime.date(2018, 11, 30), start_time=datetime.time(20, 15), end_time=datetime.time(11, 15), title='Event 1', location='Campus', notes='Lorem ipsum')
    event2 = Event(date=datetime.date(2018, 11, 8), start_time=datetime.time(14, 30), end_time=datetime.time(15, 30), title='Event 2', location='Dodge')
    event3 = Event(date=datetime.date(2018, 11, 20), start_time=datetime.time(16, 00), end_time=datetime.time(18, 00), title='Event 3')
    event4 = Event(date=datetime.date(2018, 11, 18), start_time=datetime.time(9, 00), end_time=datetime.time(11, 30), title='Event 4')
    event5 = Event(date=datetime.date(2018, 3, 18), start_time=datetime.time(12, 00), end_time=datetime.time(15, 30), title='Event 5')
    event6 = Event(date=datetime.date(2018, 7, 4), start_time=datetime.time(16, 00), end_time=datetime.time(17, 00), title='Event 6')
    event7 = Event(date=datetime.date(2018, 7, 4), start_time=datetime.time(14, 00), end_time=datetime.time(15, 00), title='Event 7')

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
    user_event12 = UserEvent(user_id=6, event_id=5, accepted=1)
    user_event13 = UserEvent(user_id=6, event_id=6, accepted=1)
    user_event14 = UserEvent(user_id=13, event_id=6, accepted=1)
    user_event15 = UserEvent(user_id=13, event_id=7, accepted=1)

    event_invite1 = EventInvitation(sender_id=1, receiver_id=2, event_id=1)
    event_invite2 = EventInvitation(sender_id=2, receiver_id=1, event_id=2)
    event_invite3 = EventInvitation(sender_id=1, receiver_id=2, event_id=3)
    event_invite4 = EventInvitation(sender_id=4, receiver_id=3, event_id=4)

    notification1 = Notification(body="New event invitation from Karen", receiver_id=2, event_id=1, type=NotificationType.event_invite)
    notification2 = Notification(body="New event invitation from Dale", receiver_id=1, event_id=2, type=NotificationType.event_invite)
    notification3 = Notification(body="New event invitation from Karen", receiver_id=2, event_id=3, type=NotificationType.event_invite)
    notification4 = Notification(body="Karen updated the details of your event - Event 4", receiver_id=2, event_id=4, type=NotificationType.event_update)
    notification5 = Notification(body="New event invitation from Jake", receiver_id=3, event_id=4, type=NotificationType.event_invite)

    avail1 = Availability(user_id=1, weekday=1, start_time=datetime.time(12, 00), end_time=datetime.time(15, 00))
    avail2 = Availability(user_id=1, weekday=4, start_time=datetime.time(9, 00), end_time=datetime.time(10, 00))
    avail3 = Availability(user_id=1, weekday=4, start_time=datetime.time(16, 00), end_time=datetime.time(18, 00))
    avail4 = Availability(user_id=1, weekday=5, start_time=datetime.time(13, 00), end_time=datetime.time(16, 30))
    avail5 = Availability(user_id=2, weekday=2, start_time=datetime.time(9, 30), end_time=datetime.time(11, 00))
    avail6 = Availability(user_id=2, weekday=3, start_time=datetime.time(15, 00), end_time=datetime.time(17, 00))
    avail7 = Availability(user_id=2, weekday=6, start_time=datetime.time(8, 00), end_time=datetime.time(11, 00))
    avail8 = Availability(user_id=6, weekday=6, start_time=datetime.time(12, 00), end_time=datetime.time(16, 00))
    avail9 = Availability(user_id=6, weekday=6, start_time=datetime.time(15, 30), end_time=datetime.time(17, 30))

    db.session.add_all([karen, dale, matt, jake, ellen, katie, dan, dan2, dan3, brian, sam, lisa, chris, blaine, emma, dylan, profile_karen, profile_dale, profile_matt, profile_jake, profile_ellen, profile_katie, profile_dan, profile_dan2, profile_dan3, profile_brian, profile_sam, profile_lisa, profile_chris, profile_blaine, profile_emma, profile_dylan, friendship1, friendship2, friendship3, friendship4, friendship5, friendship6, friendship7, friendship8, friendship9, friendship10, friendship11, friendship12, friendship13, friendship14, friendship15, friendship16, friendship17, conversation1, conversation2, conversation3, conversation4, conversation5, conversation6, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10, interest1, interest2, interest3, interest4, interest5, interest6, interest7, user_interest1, user_interest2, user_interest3, user_interest4, user_interest5, user_interest6, user_interest7, user_interest8, user_interest9, user_interest10, user_interest11, user_interest12, user_interest13, user_interest14, user_interest15, user_interest16, user_interest17, user_interest18, event1, event2, event3, event4, event5, event6, event7, user_event1, user_event2, user_event3, user_event4, user_event5, user_event6, user_event7, user_event8, user_event9, user_event10, user_event11, user_event12, user_event13, user_event14, user_event15, event_invite1, event_invite2, event_invite3, event_invite4, notification1, notification2, notification3, notification4, notification5, avail1, avail2, avail3, avail4, avail5, avail6, avail7, avail8, avail9])
    db.session.commit()
