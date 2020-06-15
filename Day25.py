# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 25 : 15-06-2020
# Day 25 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge XII - Create a Customer using OOP
#----------------------------------------------------
# what would be the output of this program ?

'''

    Create a class Customer.
    Give a name to your customer and give to your customer
    a cart and a budget.

    Let the customer fill the cart with random items available 
    in a store. 
    Assume the items are given to you through a dictionary.

    Create a function to calculate the bill of the customer at the end.
    Let the customer know if his bugdet is enough or not.


'''

class Customer:

    # initialize
    def __init__(self, name, budget):
        self.__name = name 
        self.__budget = budget
        # empty an empty cart
        self.__cart = {}
    
    # add item to cart
    def add_item_to_cart(self, item_name, item_price):
        # add key and value in dictionary
        self.__cart[item_name] = item_price
    
    # string representation of your object
    def calculate_bill(self):
        # make sure the cart is not empty
        if self.__cart :
            sum = 0
            for item in self.__cart:
                sum = sum + float(self.__cart[item])
        else :
            sum = 0
        
        if (sum > self.__budget):
            print("\nYou do not have enough money to pay this bill.")
            print("Your budget is ${}.\n".format(self.__budget))
        else:
            print("You are good to go. Your bugdet is ${}.\n".format(self.__budget))
        
        return "Your current bill is ${}.".format(sum)
    
    # string representation of your object
    def __str__(self):
        print("\nHey {}, you have the following items in your cart.".format(self.__name))
        customer = ""
        for item in self.__cart:
            customer = customer + "\nItem {} : ${}".format(item, self.__cart[item])
        return customer


if __name__ == "__main__":

    # removing the currency symbol '$' for making it easier.
    items = {
        "water" : "10",
        "biscuits" : "2",
        "chocolate" : "4",
        "rice" : "3",
        "wine" : "5"
    }

    items_bis = {
        "beer" : "25",
        "yogurt" : "34",
        "fish" : "15",
        "chicken" : "5",
        "sugar" : "8"
    }
    client = Customer("jivrik", 100)

    # add items to your chart
    for item in items :
        client.add_item_to_cart(item, items[item])
    
    # print the client
    print(client)
    # get the bill
    print(client.calculate_bill())

    # adding new items to your chart
    for item in items_bis :
        client.add_item_to_cart(item, items_bis[item])
    
    # print the client
    print(client)
    # get the bill
    print(client.calculate_bill())
    
    