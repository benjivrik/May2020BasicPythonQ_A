# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 20 : 13-06-2020
# Day 20 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge X - Create a mini-stopre using OOP
#----------------------------------------------------
# what would be the output of this program ?

'''

    Supposing your items are stored in a dictionary within 
    your class.

    Create a class Store in which you initialze an empty
    dictionary  for items and prices, and for items and the numbers of items left. 
    Give a name to your store at least.

    Add a function add_item  to update your inventory by add adding an item
    Add a function del_item  to remove an item from inventory.
    Add a function display all to display your inventory.

    Use the mini-store concept of Day 12

    Suppose that you are a store owner and you have the following items in your store

    items = {
        "water" : "10$",
        "biscuits" : "2$",
        "chocolate" : "4$",
        "rice" : "3$",
        "wine" : "5$"
    }

    add another dictionary for the numbers of items you possess in your store.
    Use the same keys as the dictionary you created for the prices. 

    
'''

class Store :

    # initialization 
    def __init__(self,name):
        # store name
        self.__name  = name
        self.__items_prices = {}
        self.__items_numbers = {}
    
    # get the name of your store
    def get_name(self):
        return self.__name
    
    # set the name of your store
    def set_name(self, name):
        self.__name = name
    
    # add an item to your store
    def add_item(self, name, price, number_of_items):
        self.__items_prices[name] = price
        self.__items_numbers[name] = number_of_items

    # remove an item
    def remove_item(self,name):
        ret = ""
        try :
            del self.__items_prices[name]
            del self.__items_numbers[name]
            ret = "\nItem '{}' successfully removed.".format(name)
        except KeyError :
            print("The item '{}' does not exist in this store.".format(name))
            ret = "Unable to remove the item {} .".format(name)

        return ret
    
    def update_inventory(self, item_name, number_of_items, action):
        '''
            int - number of items
            str - item_name
            str - action
            return none
        '''
        # assume the name is entered correctly
        # get the the current number
        current_number_of_items = int(self.__items_numbers[item_name])

        if action == "add":
            #new number of items
            new_number_of_items = current_number_of_items + number_of_items 
            #update dicitionary
            self.__items_numbers[item_name] = str(new_number_of_items)
            print("\nInventory updated for '{}'.\n>New numbers of items: {}".format(item_name,new_number_of_items))

        elif action == "sub":
            #new number of items
            #assume number_of_items is always less than current_number_of_items
            new_number_of_items = current_number_of_items - number_of_items 
            #update dicitionary
            self.__items_numbers[item_name] = str(new_number_of_items)
            print("\nInventory updated for '{}'.\n>New numbers of items: {}".format(item_name,new_number_of_items))

        else :
            print("\nPlease enter a correct action 'add' or 'sub'. You entered '{}'".format(action))


    
    # string representation of your object store
    def __str__(self):
        print("\nHey, The store {} have the following items.\n".format(self.__name))
        store = ""

        # Go through all the availables items
        # __items_prices and __items_numbers should have the same size

        for item in self.__items_prices:
            
            item_name = item # item is the key of the array
            item_price = self.__items_prices[item_name] # price
            item_quantity = self.__items_numbers[item_name] # quantity
            # line to be displayed
            line = "> Item name: {}, \n* Price: {};\n* Numbers of items: {}\n\n".format(item_name,item_price,item_quantity)
            store = store + line

        # return the string
        return store

if __name__ == "__main__":
    # add the following items in your store
    items_prices = {
        "water bottle" : "10$",
        "biscuits" : "2$",
        "chocolate" : "4$",
        "rice" : "3$",
        "wine" : "5$"
    }

    # items inventory
    items_inventory = {
        "water bottle" : "10",
        "biscuits" : "20",
        "chocolate" : "7",
        "rice" : "9",
        "wine" : "25"
    }

    # create your store
    your_store = Store("New Store")
    
    # add items in your store
    for item in items_prices :
        your_store.add_item(item, items_prices[item], items_inventory[item])
     
    # print items in your store
    print(your_store)

    # trying to remove the item "plastic bag"
    print(your_store.remove_item("plastic bag"))

    # trying to remove the item "water bottle"
    print(your_store.remove_item("water bottle"))

    # print your store with the water bottle removed
    print(your_store)

    # update the inventory for biscuits and rice
    # add 2 bags of rice and remove 3 biscuits

    # biscuits
    your_store.update_inventory('biscuits',3,'sub') 

    # rice
    your_store.update_inventory('rice',2,'add') 

    # print your store
    print(your_store)

    print("\nEnd of program.")
