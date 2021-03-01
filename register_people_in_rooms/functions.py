import pickle
from register_people.register import reading_saved_file_people
from register_of_event_rooms.register import reading_saved_file_rooms


list_peoples_in_rooms = []


def register_people_in_rooms(people, rooms):
    list_people = reading_saved_file_people()
    list_rooms = reading_saved_file_rooms()
    peoples_in_rooms = {'name': people, 'rooms': rooms}
    list_peoples_in_rooms.append(peoples_in_rooms)
    save_data_in_file(peoples_in_rooms)



def save_data_in_file(people_in_rooms) -> dict:
    file = open('peoples_in_rooms.txt', 'wb')
    pickle.dump(people_in_rooms, file)
    file.close()


def check_if_the_person_exists(people):
    list_people = reading_saved_file_people()
    print(list_people)



check_if_the_person_exists('lucas')