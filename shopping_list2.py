def welcome_msg():
    print("Welcome to to-do list!")
    print("""
Hit DONE if you are done with the list
Hit SHOW to see current list
Hit DELETE to delete an item
Hit HELP if you are scared
""")
list = []
welcome_msg()

def show_list():
    print("Here is your list!")
    count = 1
    for item in list:
        print("{}: {}".format(count, item))
        count += 1

while True:
    items = input('>  ')

    if items == 'SHOW':
        show_list()
    elif items == 'HELP':
        welcome_msg()
    elif items == "DONE":
        show_list()
        break
    elif items == "DELETE":
        show_list()
        item_index = input("Please enter the item you would like to delete or hit enter to return  ")
        if item_index:
            popped_item = list.pop(int(item_index) - 1)
            print("Removed {} from list".format(popped_item))
        continue
    else:
        item_arr = items.split(',')
        index = input("If you would like to insert these items at a certain index enter that index, otherwise press enter ")
        if index:
            spot = int(index)
            for item in item_arr:
                list.insert(spot, item.strip())
                spot += 1
        else:
            for item in item_arr:
                list.append(item.strip())
