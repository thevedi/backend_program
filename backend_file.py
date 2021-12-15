from csv import DictWriter
import csv
import pickle
import Login_page as Lp
from csv import writer
import os


def log_of_users(user_name_of_user, date_of_login, time_of_login):
    list_of_data = [user_name_of_user, date_of_login, time_of_login]
    with open('logs', 'a', newline='') as file_object:
        writer_object = writer(file_object)
        writer_object.writerow(list_of_data)


def heading(name_of_user):
    heading_to_print = "X" * 78 + "\nWelcome to Indira Gandhi International Airport\n" + f"User:{name_of_user}\n"\
                       + "X" * 78
    return print(heading_to_print)


def choice(option_one, option_two):  # Returns true or false based on choice of user
    want_to = False
    tries = 0
    try:
        while tries < 3:
            print(f"Choose an Option:",
                  f"1. {option_one}",
                  f"2. {option_two}", sep="\n")
            option_entered = int(input(":"))
            os.system('cls' if os.name == 'nt' else 'clear')
            if option_entered == 1 or option_entered == 2:
                if option_entered == 1:
                    print(f"Chosen option: {option_one}")
                    want_to = True
                    break
                else:
                    print(f"Chosen option: {option_two}")
                    break
            else:
                print("Invalid Value Entered!\n"
                      "Retry!")
                tries += 1
    except ValueError:
        print("Invalid Value, Program Ended")
        exit()
    return want_to


def read_csv(pnr_to_search):  # SEARCH FOR PNR FROM THE CSV FILE
    line_number = 0
    csv_opened = csv.DictReader(open(Lp.full_path_of_data))
    for rows in csv_opened:
        if rows["PNR"] == pnr_to_search:
            line_number = csv_opened.line_num
            print(line_number)
            sets = ["PNR", "NAME", "AGE", "COUNTRY OF ORIGIN", "DATE OF TRAVEL", "OPERATOR"]
            print("PNR found:")
            for i in sets:
                input_for_data = rows[i]
                print(f"{i}: {input_for_data}")  # Print Values as read by Text file


def write_csv(dict_of_names):  # WRITES DATA TO CSV FILE IN NEW LINE
    headers_of_csv = ["PNR", "NAME", "AGE", "COUNTRY OF ORIGIN", "DATE OF TRAVEL", "OPERATOR"]
    with open(Lp.full_path_of_data, 'a', newline='') as f_object:
        dict_object = DictWriter(f_object, fieldnames=headers_of_csv)
        dict_object.writerow(dict_of_names)


def isvalid(password_to_check):  # check whether a password is good enough
    valid_password = False
    lowercase, uppercase, special, numbers = 0, 0, 0, 0
    if len(password_to_check) >= 8:
        for letters in password_to_check:
            if letters.islower():
                lowercase += 1
            if letters.isupper():
                uppercase += 1
            if letters.isdigit():
                numbers += 1
            if letters == '@' or letters == '$' or letters == '_':
                special += 1
    if lowercase >= 1 and uppercase >= 1 and special >= 1 and numbers >= 1 and lowercase + special + uppercase\
            + numbers == len(password_to_check):
        valid_password = True
    else:
        pass
    return valid_password  # IF PASSWORD IS GOOD ENOUGH TRUE


def new_user_password_save(new_username, new_password, authorized_or_not):
    if authorized_or_not:
        try:
            with open(Lp.full_path_of_password, "rb") as opened_file:
                dict_to_hold_all_data = pickle.load(opened_file)
                dict_to_hold_all_data[new_username] = new_password  # NEW VALUE FOR NEW USERNAME
                with open(Lp.full_path_of_password, "wb") as \
                        opened_again_file:
                    pickle.dump(dict_to_hold_all_data, opened_again_file)
                    pass
        except FileExistsError:
            print("File Not Found")
    else:
        print("User not Found")


def new_user_name_save(new_username, new_name):
    try:
        with open(Lp.full_path_of_name, "rb") as opened_file:
            dict_to_hold_all_data = pickle.load(opened_file)
            dict_to_hold_all_data[new_username] = new_name  # NEW VALUE FOR NEW USERNAME
            with open(Lp.full_path_of_name, "wb") as \
                    opened_again_file:
                pickle.dump(dict_to_hold_all_data, opened_again_file)
                pass
    except FileExistsError:
        print("File Not Found")


def new_user_first_file():
    print("!!Portal for New user!!\n")
    new_username_created = Lp.get_proper_username()
    new_password = input("Password: ")
    check_password = input("Reenter password:")
    if isvalid(new_password) and new_password == check_password:
        pass
    else:
        print("Invalid Password!!")
    name_of_user = input("Enter Name:")
    return new_username_created, new_password, name_of_user


def data_entries(international_or_not):
    all_valid_input = True
    pnr_number = int(input("PNR:"))
    travel_type = "Domestic Travel"
    name_of_passenger = str.capitalize(input("Name:"))
    age = int(input("Age:"))
    if international_or_not:
        travel_type = str.capitalize(input("Enter The Country: "))
    else:
        pass
    if len(str(pnr_number)) != 10 or 1 >= age >= 99:
        all_valid_input = False
    else:
        pass
    if all_valid_input:
        return pnr_number, name_of_passenger, age, travel_type
    else:
        print("Error in saving the data!")
        exit()

