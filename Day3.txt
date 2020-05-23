# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 3 : 24-05-2020
# Day 3 | IG : https://www.instagram.com/benjivrik/
# Subject :  Challenge I - Input and user functions
#----------------------------------------------------
# what would be the output of this program ?

'''

    Request the user to enter a number.

    Use the integer entered by the user in the function that you are creating.

    This function return the double of the parameter.

'''

def double_parameter( value ):
    '''

        value here is your parameter - type int

        How to return the value from the function ?

        use 'return' as shown below.

        Mathematical operators can be applied in programming as well.

    '''
    return value * 2



#main program



user_input  = input("Enter a number : ")  #line1

user_input  = int(user_input)             #line2

print("The double is ", double_parameter(user_input))       #line3

