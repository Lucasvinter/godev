import pickle
from exception import Exception


list_rooms = []


def checking_data(name, location):
    exception = Exception()
    if(not name):
        exception.no_data()


    if(not location):
        exception.no_data()


def register_name_and_loction_in_list(name, loction):
    checking_data(name, loction)
    rooms = {'name': name, 'location': loction}
    list_rooms.append(rooms)
    save_data_in_file(rooms)


def save_data_in_file(rooms) -> dict:
    file = open('rooms.txt', 'wb')
    pickle.dump(rooms, file)
    file.close()


def reading_saved_file_rooms():
    file = open('rooms.txt', 'rb')
    rooms = pickle.load(file)
    file.close()
    list_rooms.append(rooms)
    return list_rooms





