import datetime
import pickle
from csv import writer
import os


full_path_of_password = "Usernames\\passwords_of_users"
full_path_of_name = "Usernames\\passwords_of_users"
full_path_of_data = "Data Entry\\passengers_log.csv"

def date_now():
    date_full_version = datetime.datetime.now()
    date_extracted = date_full_version.strftime("%x")
    return date_extracted


def time_now():
    date_full_version = datetime.datetime.now()
    time_extracted = date_full_version.strftime("%X")
    return time_extracted


def get_proper_username():
    counter = 0
    username = ""
    while counter <= 2:
        try:
            username = int(input("Username:"))
            if len(str(username)) == 8:
                return str(username)
            else:
                print("Invalid Username Format",
                      "Reenter username!", sep="\n")
                counter += 1
        except ValueError:
            print("Invalid Input")
            counter += 1


def find_password_for_username(entered_username):
    with open(full_path_of_password, "rb") as opener:
        password_obtained = ""
        try:
            loaded_dictionary = pickle.load(opener)
            password_obtained = loaded_dictionary.get(entered_username)
        except EOFError:
            default_key = {"12345678": "Default@00"}
            with open(full_path_of_password, "wb") as file_to_write:
                print("Files Set to default")
                pickle.dump(default_key, file_to_write)
                file_to_write.close()
        return password_obtained


def authorize_user(password):
    authorized, password_entered, tries = False, "", 0
    while tries < 3:
        password_entered = input("Password: ")
        if password_entered == password:
            authorized = True
            break
        else:
            print("Password is incorrect!\nRetry!\r")
            tries += 1
    return authorized


def get_name_of_user(username):
    file_to_read = open(full_path_of_name, "rb")
    loaded_dict = pickle.load(file_to_read)
    file_to_read.close()
    name_found = loaded_dict.get(username)
    return name_found


def log_data(user_name, date, time_of_login):
    list_data = [user_name, date, time_of_login]
    with open('logs', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        f_object.close()

