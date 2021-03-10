# Shopping list
shopping_list = []


# Menu
def menu_serve():
    print('''
    Choose an option:
    1. Add Item
    2. Remove Item
    3. Show List
    4. Quit
            ''')

# Add item


def add_item(item_name):
    shopping_list.append(item_name)
    print(f'{item_name} added to list\n {shopping_list}')


# remove item

def remove_item(item_name):
    shopping_list.remove(item_name)
    print(f'{item_name} removed from list\n {shopping_list}')
# see all items


def print_list():
    print([i for i in shopping_list])


# quit program

def quit_prog():
    print("Quiting Program")


if __name__ == "__main__":
    while True:
        menu_serve()
        try:
            input_frm_user = int(input("Enter choice: "))
            if input_frm_user == 1:
                item = input("Enter item name: ")
                add_item(item)
            elif input_frm_user == 2:
                item = input("Enter item name: ")
                remove_item(item)
            elif input_frm_user == 3:
                print_list()
            elif input_frm_user == 4:
                quit_prog()
                break
            else:
                continue
        except ValueError as e:
            print("Bakwass Input")
