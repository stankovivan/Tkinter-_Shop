from json import loads, dump
from tkinter import Entry, Button

from Animal_Shop.pass_hashing import hash_pass
from animals_page import display_animals
from validator import password_validator
from main import frame, root
from cleaner import screen_clean


def get_users_data():
    info = []
    with open("test_db/user_info.json", "r") as users_file:
        for line in users_file:
            info.append(loads(line))
    return info


def reverse_back():
    screen_clean()
    entry()


def entry():
    register_button = Button(
        root,
        text='Register',
        bg='limegreen',
        fg='black',
        borderwidth=0,
        width=25,
        height=5,
        command=register,
    ),

    login_button = Button(
        root,
        text="Login",
        bg="mediumblue",
        fg="white",
        width=25,
        height=5,
        bd=1,
        command=login,
    )

    frame.create_window(350, 390, window=register_button)
    frame.create_window(350, 300, window=login_button)
    frame.create_text(
        350,
        80,
        text="Welcome to Animal Shop",
        font=('Helvetica', 18, 'bold'),
        fill='black',

    )
    return frame


def register():
    screen_clean()

    frame.create_text(
        100,
        50,
        text="First name:",
        font=('Helvetica', 12, 'bold'),

    )
    frame.create_text(
        100,
        100,
        text="Last name:",
        font=('Helvetica', 12, 'bold'),
    )
    frame.create_text(
        100,
        150,
        text="Username:",
        font=('Helvetica', 12, 'bold'),
    )
    frame.create_text(
        100,
        200,
        text="Password:",
        font=('Helvetica', 12, 'bold'),
    )

    frame.create_window(
        230,
        50,
        window=first_name_entry_box,
        height=25,
        width=150,
    )
    frame.create_window(
        230,
        100,
        window=last_name_entry_box,
        height=25,
        width=150,
    )
    frame.create_window(
        230,
        150,
        window=username_entry_box,
        height=25,
        width=150,
    )

    frame.create_window(
        230,
        200,
        window=password_entry_box,
        height=25,
        width=150,
    )

    registration_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        height=3,
        width=10,
        border=0,
        command=registration
    )

    frame.create_window(300, 250, window=registration_button)

    go_back_button = Button(
        root,
        text="Back",
        bg="red",
        fg="white",
        height=3,
        width=10,
        border=0,
        command=reverse_back
    )

    frame.create_window(380, 250, window=go_back_button)


def registration():

    information_dict = {
        "first_name": first_name_entry_box.get(),
        "last_name": last_name_entry_box.get(),
        "username": username_entry_box.get(),
        "password": hash_pass(password_entry_box.get()),
        "animals": []
    }

    if check_registration(information_dict):
        with open("test_db/user_info.json", "a") as users_file:
            dump(information_dict, users_file)
            users_file.write("\n")
            display_animals()


def check_registration(info):
    counter = 0
    error_message = "All fields are required"
    message = "Password should have uppercase, lowercase, one numeral and have at least 5 characters"
    for element in list(info.values())[:-1]:
        counter += 1
        x = 300
        y = 300
        if counter == 4:
            result = password_validator(element)
            if not result:
                frame.delete("error")
                frame.create_text(
                    x,
                    y,
                    text=message,
                    fill="red",
                    tags="error"
                )

        if element.strip() == '':
            frame.create_text(
                300,
                300,
                text=error_message,
                fill="red",
                tags="error"
            )
            return False
    frame.delete("error")

    # Jason file needs to be on one line!
    info_data = get_users_data()
    for i in range(len(info_data)):
        if info_data[i]['username'] == info['username']:
            frame.create_text(
                300,
                300,
                text="Username already exists.",
                fill="red",
                tag="error",
            )
            return False
    frame.delete("error")
    return True


def login():
    screen_clean()

    frame.create_text(
        100,
        150,
        text="Username:",
        font=('Helvetica', 12, 'bold'),
    )
    frame.create_text(
        100,
        200,
        text="Password:",
        font=('Helvetica', 12, 'bold'),
    )

    frame.create_window(
        230,
        150,
        window=username_entry_box,
        height=25,
        width=150,
    )
    frame.create_window(
        230,
        200,
        window=password_entry_box,
        height=25,
        width=150,
    )
    logging_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        height=3,
        width=10,
        border=0,
        command=login_success
    )

    frame.create_window(
        300,
        250,
        window=logging_button,
    )

    go_back_button = Button(
        root,
        text="Back",
        bg="red",
        fg="white",
        height=3,
        width=10,
        border=0,
        command=reverse_back
    )

    frame.create_window(380, 250, window=go_back_button)


def login_success():
    if check_loging():
        display_animals()

    else:
        frame.create_text(
            200, 300,
            text="Invalid username or password",
            fill="red",
        )


def check_loging():
    info_data = get_users_data()
    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == username_entry_box.get() and password == hash_pass(password_entry_box.get()):
            return True
    return False


first_name_entry_box = Entry(root, bd=0)
last_name_entry_box = Entry(root, bd=0)
username_entry_box = Entry(root, bd=0)
password_entry_box = Entry(root, bd=0, show="*")
