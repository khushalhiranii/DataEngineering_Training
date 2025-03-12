def create_list():
    return []

def update_list(element, lst):
    lst.append(element)

def remove_from_list(element, lst):
    lst.remove(element)

new_list = create_list()

while True:
    operation = int(input(
        'Enter 1 to add an element, 2 to remove an element, '
        '3 to search for an element, 4 to print the list, 5 to exit: '
    ))
    if operation == 1:
        element = input()
        update_list(element ,new_list)
    elif operation == 2:
        element = input()
        remove_from_list(element ,new_list)
    elif operation == 3:
        element = input()
        if element in new_list:
            print(new_list.index(element))
        else:
            print('Element not found')
    elif operation == 4:
        print(new_list)
    elif operation == 5:
        print('Exiting')
        break
    else:
        print('Invalid input')
