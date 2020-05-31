# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 12 : 2-06-2020
# Day 12 | IG : https://www.instagram.com/benjivrik/
# Subject : Dictionaries
#----------------------------------------------------
# what would be the output of this program ?

'''

    Internet > a collection of unordered and changeable data.

    You can associate a keyword to its content, 
    similar to when you use a conventional dictionary
    in which a specific word is associate to its definition.

    Syntax of dictionary ?

    var =  { 'keyword' : 'content' }

    Let's create a 'mini store inventory' showing the prices of the items. 
    And let the user choose the price of an item in your store.

'''

# your items

items = {
    "water" : "10$",
    "biscuits" : "2$",
    "chocolate" : "4$",
    "rice" : "3$",
    "wine" : "5$"
}

user_name = input("Hey, what is your name ?")

print("Hello {}, I have the following items in my store.".format(user_name))
#item id
item_id = 1
#display items
for item in items :
  print("> Item {} : {}".format(item_id,item))
  item_id = item_id + 1

#main program

stop = "no"

while stop == 'no' :  #this is a loop with a condition
    print("Which item price do you wanna check ?")
    user_choice  = input("Enter your item name : ")
    while not user_choice in items :
      user_choice  = input("I do not have the item {}. Please enter a correct item: ".format(user_choice))

    print("Thank you. The price for your item {} is {}".format(user_choice, items[user_choice]))
    #ask the user if he wants to contine
    stop = input("Do you wanna stop ? yes or no : ") #line10
    if(stop != "yes"):
        stop = "no"
    else :
        break #stop the loop    


#outside_the_loop            
print("End of program")

