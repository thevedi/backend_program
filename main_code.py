import time
import Login_page as Lp
import backend_file as back
import os


#  HEADING
print("x" * 70, "Indira Gandhi International Airport", "Authorization Terminal", "x" * 70, sep='\n')
#  ASK FOR USERNAME
username_of_authorized_person = Lp.get_proper_username()
status_of_user = Lp.authorize_user(Lp.find_password_for_username(username_of_authorized_person))
name_of_user = Lp.get_name_of_user(username_of_authorized_person)
back.log_of_users(str.upper(name_of_user), Lp.date_now(), Lp.time_now())
# LOGGING DATA OF USERS
if back.choice("Create a New User", "Data Management"):
    back.heading(name_of_user)
    new_username, new_password, new_name = back.new_user_first_file()
    back.new_user_password_save(new_username, new_password, status_of_user)
    back.new_user_name_save(new_username, new_name)
    print("New User Created Successfully!")
    exit()
else:  # DATA ENTRY OR SEARCH DATA
    blank_dict = {}
    counter, permission = 0, ""
    while counter <= 10 or permission != "exit":
        back.heading(name_of_user)
        if back.choice("DATA ENTRY", "SEARCH PNR"):
            pnr_number, name_of_passenger, age, travel_type \
                = back.data_entries(back.choice("International Terminal", "Domestic Terminal"))
            counter += 1
            permission = input("Type exit to EXIT the Terminal else press Enter to Proceed!")
            blank_dict["PNR"] = pnr_number
            blank_dict["NAME"] = str.upper(name_of_passenger)
            blank_dict["AGE"] = age
            blank_dict["COUNTRY OF ORIGIN"] = str.upper(travel_type)
            blank_dict["DATE OF TRAVEL"] = Lp.date_now()
            blank_dict["OPERATOR"] = str.upper(name_of_user)
            print("Data Saved Successfully!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            back.write_csv(blank_dict)
        else:
            back.read_csv(input("Enter PNR to search: "))
            permission = input("Type exit to EXIT the Terminal else press Enter to Proceed!")
            counter += 1
