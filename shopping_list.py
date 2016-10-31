# Shopping list to help with your groceries

list = []

def welcome_msg():
    print("Welcome to to-do list!")
    print("""
Hit DONE if you are done with the list
Hit SHOW to see current list
Hit HELP if you are scared
""")

def reminder():
    print("Here is your list:")
    for bullet in list:
        print(bullet)

def append_item(bullet):
    list.append(item)
    if len(list) == 1:
        print("""Added "{}" to list. 1 total item""".format(bullet))
    else:
        print("""Added "{}" to list. {} total items""".format(bullet, len(list)))

welcome_msg()

while True:
    item = input("Add item: ")

    if item == 'DONE':
        break
    elif item == 'HELP':
        welcome_msg()
        continue
    elif item == 'SHOW':
        reminder()
        continue
    else:
        append_item(item)


reminder()
