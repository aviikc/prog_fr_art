# Made by .............
# Date
# Display App Name
# Short Intro to what the app does
# Insert todo content (Today, tomorrow, date)
# Modify todo content (Today, tomorrow, date)
# Display todo content (Today, tomorrow, date/ dates)
# Exit

from random import choice
import sys
from datetime import date, timedelta
from todos.format_validadors import *
from todos.todos import ToDo
from todos.menus import Menus

VERSION = 1.0
FORMAT = "YYYY-MM-DD"

def insert_data():
    while(True):
        print(menus.insert_note_menu())
        try:
            choice = int(input("Enter insertion choice: "))
            if choice == 1:
                content = input("Enter content in 30 words: ").lstrip().rstrip()
                if parse_content(content):
                    date_today = date.today()
                    new_todo = ToDo(date_today)
                    new_todo.note = content
                    print(new_todo)
                    print("Todo note added!")
                    break
            elif choice == 2:
                content = input("Enter content in 30 words: ").lstrip().rstrip()
                if parse_content(content):
                    date_tomrw = date.today() + timedelta(days=1)
                    new_todo = ToDo(date_tomrw)
                    new_todo.note = content
                    print(new_todo)
                    print("Todo note added!")
                    break
            elif choice == 3:
                while(True):
                    some_date = input(f"Enter date in {FORMAT} format: ")
                    if parse_date_string(some_date):
                        date_ = date(int(some_date.split("-")[0]),
                                    int(some_date.split("-")[1]),
                                    int(some_date.split("-")[2]))
                        break
                    else:
                        continue
                content = input("Enter content in 30 words: ").lstrip().rstrip()
                if parse_content(content):
                    new_todo = ToDo(date_)
                    new_todo.note = content
                    print(new_todo)
                    print("Todo note added!")
                    break
            elif choice == 4:
                break
            else:
                print("Enter 1,2,3 or 4")
                continue
        except ValueError:
            print("Bad Input!!!")

def modify_data():
    pass


def display_data():
    pass


choices = {1:insert_data,
           2:modify_data,
           3:display_data
           }

if __name__ == "__main__":
     # Display App Name
    print("========================")
    print(f"ToDo App Version {VERSION}\n")
    # Short Intro to what the app does
    print(("App to create a todo list to \nprioritize your commitments"))
    print("========================\n")
    menus = Menus()
    while(True):
        print(menus.main_menu())
        try:
            user_inp = input("Your choice: ")
            choice = int(user_inp)
            if choice in choices:
            # print("choice is", choice)
                action = choices.get(choice)
                action()
            else:
                print("Unknown Input")
        except ValueError:
            if user_inp == 'q' or user_inp == 'Q':
                # choice = user_inp
                print("Thank you for using the ToDo App.")
                sys.exit(1)
        else:
            print("Unknown Input")




