from app.models import *

def example_data():
    karen = User(username='karen', email='karen@example.com', fname='Karen', lname='Smith')
    karen.set_password('karen')
    dale = User(username='dale', email='dale@example.com', fname='Dale', lname='Sue')
    dale.set_password('dale')
    matt = User(username='matt', email='matt@example.com', fname='Matt', lname='Anderson')
    matt.set_password('matt')
    jake = User(username='jake', email='jake@example.com', fname='Jake', lname='Brown')
    jake.set_password('jake')
    ellen = User(username='ellen', email='ellen@example.com', fname='Ellen', lname='James')
    ellen.set_password('ellen')
    katie = User(username='katie', email='katie@example.com', fname='Katie', lname='Wolf')
    katie.set_password('katie')
    dan = User(username='dan', email='dan@example.com', fname='Dan', lname='Kay')
    dan.set_password('dan')

    profilekaren = Profile(user_id = 1)
    profiledale = Profile(user_id = 2)
    profilematt = Profile(user_id = 3)
    profilejake = Profile(user_id = 4)
    profileellen = Profile(user_id = 5)
    profilekatie = Profile(user_id = 6)
    profiledan = Profile(user_id = 7, about = "" )


    friendship1 = Friends(user_id_1=1, user_id_2=2, status=FriendStatus.accepted)
    friendship2 = Friends(user_id_1=3, user_id_2=4, status=FriendStatus.requested)
    friendship3 = Friends(user_id_1=5, user_id_2=7, status=FriendStatus.accepted)
    friendship4 = Friends(user_id_1=6, user_id_2=5, status=FriendStatus.accepted)
    friendship5 = Friends(user_id_1=6, user_id_2=7, status=FriendStatus.accepted)

    conversation1 = Conversation(user_id_1=1, user_id_2=2)
    conversation2 = Conversation(user_id_1=4, user_id_2=1)
    message1 = Message(sender=1, conversation_id=1, body='hello', read=True)
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

    db.session.add_all([karen, dale, matt, jake, ellen, katie, dan, profilekaren, profiledale, profilematt, profilejake, profileellen, profilekatie, profiledan, friendship1, friendship2, friendship3, friendship4, friendship5, conversation1, conversation2, message1, message2, message3, interest1, interest2, interest3, interest4, user_interest1, user_interest2, user_interest3, user_interest4, user_interest5, user_interest6, user_interest7, user_interest8, user_interest9, user_interest10, user_interest11, user_interest12])
    db.session.commit()
