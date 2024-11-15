import requests
import json


### This lists all the different craft activities OR craft items, depending how it is used ###
def display_crafts(activity_or_item):
    result = requests.get(
        f'http://127.0.0.1:5000/crafts/{activity_or_item}', headers={"content-type": "application/json"}
    )
    return result.json()


### This shows what is required for a craft activity ###
def display_craft_activity(craft):
    result = requests.get(
        f'http://127.0.0.1:5000/crafts/craft_activity/{craft}', headers={"content-type": "application/json"}
    )
    return result.json()


### Shows information about specific craft items ###
def display_craft_item(craft_item):
    result = requests.get(
        f'http://127.0.0.1:5000/crafts/craft_item/{craft_item}', headers={"content-type": "application/json"}
    )
    return result.json()


### Adds a new craft type ###
def add_new_craft(craft):
    result = requests.post(
        'http://127.0.0.1:5000/crafts', headers={"content-type": "application/json"}, data=json.dumps(craft)
    )
    return result.json()


### Creates the new craft table ###
def add_new_craft_table(craft_activity):
    result = requests.post(
        'http://127.0.0.1:5000/crafts/craft_activity', headers={"content-type": "application/json"},
        data=json.dumps(craft_activity)
    )
    return result.json()


### Adds items to the new craft table ###
def add_new_craft_data(list_of_craft):
    result = requests.put(
        'http://127.0.0.1:5000/crafts/craft_activity/item', headers={"content-type": "application/json"},
        data=json.dumps(list_of_craft)
    )
    return result.json()


### Adds new items to their item tables ###
def update_craft_item(craft_data):
    result = requests.put(
        'http://127.0.0.1:5000/crafts/craft_item', headers={"content-type": "application/json"},
        data=json.dumps(craft_data)
    )
    return result.json()


### Adds a new item type to the craft_item table ###
def update_craft_item_table(item_name):
    result = requests.put(
        'http://127.0.0.1:5000/crafts/craft_item_table', headers={"content-type": "application/json"},
        data=json.dumps(item_name)
    )
    return result.json()


### Function for adding a new item to a table ###
def add_to_item_table(item):
    info_list = []
    item = item.title()
    if item == "Wool":
        info_list.append(item.lower())
        item_type = input("What type of wool is it? e.g. chunky ")
        info_list.append(item_type)
        material = input("What material is the wool? e.g. 100% wool ")
        info_list.append(material)
        colour = input("What colour is the wool? ")
        info_list.append(colour)
        weight = input("What is the weight of the wool in grams? e.g. 100 ")
        info_list.append(weight)
        item_use = input("What could you use the wool for? e.g. crochet ")
        info_list.append(item_use)
    elif item == "Thread":
        info_list.append(item.lower())
        item_type = input("What type of thread is it? e.g. Embroidery thread ")
        info_list.append(item_type)
        colour = input("What colour is the thread? ")
        info_list.append(colour)
    elif item == "Paper":
        info_list.append(item.lower())
        item_size = input("What size is the paper? e.g. A4 ")
        info_list.append(item_size)
        colour = input("What colour is the paper? ")
        info_list.append(colour)
        weight = input("What is the weight of the paper in GSM? e.g. 140 ")
        info_list.append(weight)
    elif item == "Card":
        info_list.append(item.lower())
        item_size = input("What size is the card? e.g. A4 ")
        info_list.append(item_size)
        colour = input("What colour is the card? ")
        info_list.append(colour)
        weight = input("What is the weight of the card in GSM? e.g. 260 ")
        info_list.append(weight)
    elif item == "Machine sewing needle":
        info_list.append(item.lower())
        item_type = input("What type of machine sewing needle is it? e.g. quilting ")
        info_list.append(item_type)
    elif item == "Knitting needle":
        info_list.append(item.lower())
        item_type = input("What type of knitting needle is it? e.g. straight ")
        info_list.append(item_type)
        size = input("What size knitting needle is it in mm? e.g. 5 ")
        info_list.append(size)
        item_use = input("Which weight of wool is this knitting needle best for? e.g. lightweight ")
        info_list.append(item_use)
    elif item == "Hand sewing needle":
        info_list.append(item.lower())
        item_type = input("What type of hand sewing needle is it? e.g. darning ")
        info_list.append(item_type)
    elif item == "Fabric":
        info_list.append(item.lower())
        item_type = input("What type of fabric is it? e.g. cotton ")
        info_list.append(item_type)
        pattern = input("What pattern does the fabric have? (if plain, put 'plain') ")
        info_list.append(pattern)
        colour = input("What is the main colour of the fabric? ")
        info_list.append(colour)
        item_use = input("What is this fabric best used for? e.g. quilting ")
        info_list.append(item_use)
    else:
        print("I will ask for the type, the colour and the use of the new item.")
        info_list.append(item.lower())
        item_type = input(f"What type of {item} is it? ")
        info_list.append(item_type)
        colour = input(f"What colour is {item}? ")
        info_list.append(colour)
        item_use = input(f"What do you use {item} for? ")
        info_list.append(item_use)

    # print(info_list)
    update_craft_item(info_list)
    print(display_craft_item(item.lower()))

    craft_item_list = display_crafts("craft_items")

    new_craft_list = []
    for i in craft_item_list:
        new_craft_list.append(i[0])

    if item.title() not in new_craft_list:
        update_craft_item_table(item)

    new_craft_item_list = display_crafts("craft_items")

    for i in new_craft_item_list:
        new_craft_list.append(i[0])

    print()
    print(f"{item} has been added to the database.")
    #print(display_crafts("craft_items"))

def run():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Hello and welcome to crafting world!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("~~~~~~~~~ CRAFTS AVAILABLE ~~~~~~~~~")
    craft = display_crafts("craft_type")
    for i in craft:
        print(i)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    question = input("Would you like to find a craft (find), add a new one (new) or exit (exit): ")
    while question != "exit":
        if question == "find":
            print("You entered 'find'")
            find_craft = (input("Please enter the craft you would like information on: ").lower()).replace(" ", "_")
            print()
            craft_list = (((str(display_crafts("craft_type"))).replace("[", "")).replace("'", "")).replace("]", "")
            if (find_craft.title()).replace("_", " ") not in craft_list:
                print()
                print("Please check the spelling of the craft. ")
                print()
                find_craft = (input("Please enter the craft you would like information on: ").lower()).replace(" ", "_")

            craft_list = display_craft_activity(find_craft)
            print()
            print(craft_list)
            print()
            more_info = input("Would you like to find out more about any of the craft items? y/n ")
            print()
            while more_info != "n":
                if more_info == "y":
                    all_items = display_crafts("craft_items")
                    all_item_list = ""
                    for i in all_items:
                        all_item_list = all_item_list + i[0] + ", "

                    more_craft_info = (input("Which item, from the craft's item list, would you like more information "
                                             "on? ").lower())
                    print()

                    while more_craft_info.title() not in all_item_list.title():
                        print("Must be a craft from the list. If the craft is new and you have not entered the new item yet, please enter it under 'new' then 'item'.")
                        more_craft_info = (input("Which item, from the craft's item list, would you like more information "
                                                 "on? ").lower())

                    # print(all_item_list)
                    print(display_craft_item(more_craft_info))
                    more_info = input("Would you like to find out more about any of the craft items? y/n ")
                else:
                    print("Please enter 'y' or 'n'.")
                    more_info = input("Would you like to find out more about any of the craft items? y/n ")

            question = input("Would you like to find a craft (find), add a new one (new) or exit (exit): ")

        elif question == "new":
            print("You entered 'new'")
            craft_or_item = input("Would you like to add a new craft (craft) or add a new craft item (item)? ")
            while craft_or_item != "item":
                if craft_or_item == "craft":
                    new_craft = input("What is the name of your new craft? ")
                    if new_craft.title() in craft:
                        print("Please enter a new craft.")
                        new_craft = input("What is the name of your new craft? ")
                    check = input(f"You want to enter {new_craft} to the database? y/n ")
                    if check != "y":
                        break
                    add_new_craft(new_craft.title())
                    add_new_craft_table(new_craft)
                    print(f"{new_craft.title()} has been added to the database.")

                    add_item = "y"
                    while add_item == "y":
                        print("You will be asked for the item and type. If there are options for type, please put "
                              "'your choice' ")
                        item = (input("What is the item? e.g. thread ")).title()
                        item_type = input("What is the type? e.g. embroidery ")

                        craft_item_list = []
                        craft_item_list.append(new_craft)
                        craft_item_list.append(item)
                        craft_item_list.append(item_type)
                        print(craft_item_list)
                        add_new_craft_data(craft_item_list)

                        add_item = input(f"Do you have more craft items to add to {new_craft.title()}? y/n ")

                    craft_or_item = "item"
                else:
                    print("Please enter 'craft' or 'item'.")
                    craft_or_item = input("Would you like to add a new craft (craft) or add a new craft item (item)? ")
            while craft_or_item == "item":
                update = input("Would you like to enter a new item? y/n ")
                if update != "y":
                    break
                item = input("What is the name of your item? ")
                add_to_item_table(item)
                another = input("Would you like to add another item? y/n ")
                while another != "n":
                    if another == "y":
                        item = input("What is the name of your item? ")
                        add_to_item_table(item)
                    else:
                        print("Please enter 'y' or 'n'.")
                        another = input("Would you like to add another item? y/n ")
                while another == "n":
                    break
                break
            question = input("Would you like to find a craft (find), add a new one (new) or exit (exit): ")
        else:
            print("Please enter 'find', 'new' or 'exit'.")
            question = input("Would you like to find a craft (find), add a new one (new) or exit (exit): ")

    print("Thank you for using this service!")


if __name__ == '__main__':
    run()