from flask import Flask, render_template, request, redirect
from register_people.register import register_name_and_surname_in_the_list, list_people, reading_saved_file
from register_of_event_rooms.register import register_name_and_loction_in_list, list_rooms
from register_coffe_space.register import register_space_and_loction_in_list, list_space


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register_people')
def register_people():
    return render_template('people.html')


@app.route('/register_rooms')
def register_rooms():
    return render_template('rooms.html')


@app.route('/register_space')
def register_space():
    return render_template('space.html')


@app.route('/save_people')
def save_people():
    name = request.args['name']
    surname = request.args['surname']
    register_name_and_surname_in_the_list(name, surname)
    return redirect('/list_people')


@app.route('/save_rooms')
def save_rooms():
    name = request.args['name']
    location = request.args['location']
    register_name_and_loction_in_list(name, location)
    return redirect('/list_rooms')


@app.route('/save_space')
def save_space():
    space = request.args['space']
    location = request.args['location']
    register_space_and_loction_in_list(space, location)
    return  redirect('/list_space')


@app.route('/list_people')
def lista_people():
    reading_saved_file()
    return render_template('list_people.html', lista=list_people)


@app.route('/list_rooms')
def lista_rooms():
    return render_template('list_rooms.html', lista=list_rooms)


@app.route('/list_space')
def lista_space():
    return render_template('list_space.html', lista=list_space)

app.run()