import pickle
from exception import Exception


list_space = []


def checking_data(space, location):
    exception = Exception()
    if(not space):
        exception.no_data()


    if(not location):
        exception.no_data()


def register_space_and_loction_in_list(space, loction):
    checking_data(space, loction)
    space = {'space': space, 'location': loction}
    list_space.append(space)
    save_data_in_file(space)


def save_data_in_file(space) -> dict:
    file = open('space.txt', 'wb')
    pickle.dump(space, file)
    file.close()






