# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 8 : 29-05-2020
# Day 8 | IG : https://www.instagram.com/benjivrik/
# Subject : Modules -  Random
#----------------------------------------------------
# what would be the output of this program ?

'''

    Internet > Modules are python files with python code.

    You don't have to rewrite existing built-in python functions
    such as mathematical modules.

    Let's use the module random;

    This module helps you to generate random number.

    How do you insert a module in my code ?
    > use the keyword import.

    Each module has its own functions inside.

    Let's generate 5 five random  numbers between 0 and 10, five times

    We are going to use the function randint(a,b) of random

    
'''

#main program


import random

iterations  = 5 #number of iteration

#randint parameters

lower_limit = 0     #lower limit
upper_limit = 10    #upper limit

stop = "no"

while stop == "no":
    
    for i in range(iterations) : #loop going from 0 to iterations-1
        #inside the loop
        print("Number {} : {}".format(i+1, random.randint(lower_limit,upper_limit)))

    #ask the user if he wants to contine
    stop = input("Do you wanna stop ? yes or no : ")
    if(stop != "yes"):
        stop = "no"
    else :
        break #stop the loop   


#outside the loop            
print("End of program")






