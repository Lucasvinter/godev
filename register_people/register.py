import pickle
from exception import Exception


list_people = []


def checking_data(name, surname):
    exception = Exception()
    if(not name):
        exception.no_data()


    if(not surname):
        exception.no_data()


def register_name_and_surname_in_the_list(name, surname):
    checking_data(name, surname)
    people = {'name': name, 'surname': surname}
    save_data_in_file(people)


def save_data_in_file(people) -> dict:
    file = open('people.txt', 'wb')
    pickle.dump(people, file)
    file.close()


def reading_saved_file_people():
    file = open('people.txt', 'rb')
    people = pickle.load(file)
    file.close()
    list_people.append(people)
    return list_people






