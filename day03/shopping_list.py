'''
Shopping list application with data save feature
'''
import datetime
import random
import os


# shopping_cart_id
# print(datetime.datetime.now())
date_id = "".join(
    "".join(datetime.datetime.now().strftime("%D%T").split("/")).split(":"))
rand_id = random.randint(100, 999)
shopping_cart_id = str(date_id) + str(rand_id)
print(f'Order for Shopping cart ID: {shopping_cart_id}')


# shopping_cart
shopping_cart = []

# shopping_carts_list
shopping_cart_list = {}

# Menu


def menu():
    print('''
    1.   Add Item
    2.   Remove Item
    3.   Show List
    4.   Flush Current List
    5.   Show All Records by Date
    6.   Retrive an old List
    "m"  Show menu
    "q"  Quit
    ''')

# Add item


def add_item(item):
    if item not in shopping_cart:
        shopping_cart.append(item)
        print(shopping_cart)
    else:
        print("Item already in list")

# Remove Item


def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(shopping_cart)
    else:
        print(f'There is no {item} in list')
        pass

# See Items


def show_cart():
    for x in shopping_cart:
        print(x)


# Save shopping cart
def file_write(a, b):
    with open('shopping_cart.txt', 'a') as abc:
        abc.write("{} {}\n".format(a, b))


# Retrieve Shopping Carts of a given id
def read_shopping_cart():
    # print("Feature coming up!")
    with open('shopping_cart.txt', 'r') as shopping_list_import:
        sl = shopping_list_import.readlines()
        return sl


def read_update_data():
    if os.path.isfile("shopping_cart.txt"):
        j = read_shopping_cart()
        for i in j:
            r = "".join(i.split(" ")[1:]).rstrip("\n")[
                1:-1].replace("'", "").split(",")
            shopping_cart_list[int(i.split(" ")[0])] = r
           # shopping_cart_list[i.split(" ")[0]] = i.split(" ")[1]
            #            shopping_cart_list[i.split("/")[0].split(":")[0]] = i.split("/")[0].split(":")[1]


def retrive_list(s_id):
    if s_id in shopping_cart_list:
        print(shopping_cart_list[s_id])
    else:
        print("Invalid Key")


if __name__ == "__main__":
    read_update_data()
    menu()
    while True:
        try:
            user_input = input("Enter choice: ")
            if user_input == "1":
                item_name = input("Name of item: ")
                add_item(item_name)
            elif user_input == "2":
                item_name = input("Name of item: ")
                remove_item(item_name)
            elif user_input == "3":
                show_cart()
            elif user_input == "4":
                shopping_cart = []
            elif user_input == "5":
                for key, value in shopping_cart_list.items():
                    print("Id:{}  Items: {}".format(key, value))
            elif user_input == "6":
                c_id = int(input("Enter a valid shopping id: "))
                retrive_list(c_id)
            elif user_input.lower() == "m":
                menu()
                continue
            elif user_input == "q" or user_input == "Q":
                if len(shopping_cart) != 0:
                    opt = input("Save before quiting? ['y'/'n']: ")
                    if opt.lower() == 'y':
                        file_write(shopping_cart_id, shopping_cart)
                        print(
                            f'Shopping cart data updated for {shopping_cart_id}')
                    elif opt.lower() == 'n':
                        break
                print("Bye!!!!")
                break
            else:
                continue
        except ValueError as e:
            print(e)
