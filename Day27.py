# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 27 : 17-06-2020
# Day 27 | IG : https://www.instagram.com/benjivrik/
# Subject : 5 Products Objects for 2 Two Customers
#----------------------------------------------------
# what would be the output of this program ?

'''

    Create 5 Products object from Day26 and create two customers.
    Assign the budget to the Customer from Day25 and let
    them know if they have enough money to buy them.

    Add your products in a the Customer's cart.

'''

import Day26
import Day25

# products list
products = list()

# creating products
product_one =  Day26.Product('banana',54,7)
product_two =  Day26.Product('pineapple',32,5)
product_three = Day26.Product('orange',21,8)
product_four = Day26.Product('wine',36,2)
product_five = Day26.Product('beer',10,9)

# adding products in the products list
products.append(product_one)
products.append(product_two)
products.append(product_three)
products.append(product_four)
products.append(product_five)

# printing the products
for product in products :
    print(product)


# creating creating customers
customer_one = Day25.Customer("Benji", 400)
customer_two = Day25.Customer("Tom",100)

# adding items to customers
for product in products:
    # product name
    product_name = product.get_name()
    # product price
    product_price = product.get_price()
    # giving items to the customer
    customer_one.add_item_to_cart(product_name, product_price)
    customer_two.add_item_to_cart(product_name, product_price)


# printing the customers items

print(customer_one) # customer one
# printing the bill of the customer
print(customer_one.calculate_bill()) # customer one


# printing the bill of the customer
print(customer_two) # customer two
print(customer_two.calculate_bill()) # customer two
