# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 9 : 30-05-2020
# Day 9 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge III - Guess the number
#----------------------------------------------------
# what would be the output of this program ?

'''

    Let the user guess the number you have just generated.
    Your  number should be generated between 0 and 10.

    if the value entered is higher  than the number
    let the user know so that the user can reduce its value
    for the next attempt.

    if the value entered is lower than the number
    let the user know so that the user can increase its
    value.

    Give 5 attemps to the user.
    If the user fails to find the number,
    ask the user if he wants to stop.

    If the user enter yes, stop program.
    
'''

#main program


import random

attempt = 5 #number of attempt

#randint parameters

lower_limit = 0     #lower limit
upper_limit = 10    #upper limit

stop = "no"

while stop == "no":

    # generate new number
    number = random.randint(lower_limit,upper_limit)

    print("Hello User. Guess the number I have just generated.")
    
    # while loop for the user attempt
    while attempt > 0 :

        print("you have {} attempt(s) left.".format(attempt))
        
        user_input = input("Enter a value (integer) : ")

        user_input = int(user_input)

        if( user_input >  number ) :

            print("Your value is higher than expected.")

        elif ( user_input < number ):

            print("Your value is lower than expected.")

        else :

            print(
              """
              Congrats!
              You entered {} and
              the correct number  is also {}!\n""".format(user_input,number)
              )
            break

        attempt = attempt - 1

    # ask the user if he wants to continue
    stop = input("Do you wanna stop ? yes or no : ") 
    if(stop != "yes"):
        stop = "no"
        attempt = 5 #reinitialize the attempt
    else :
        break #stop the loop   


#outside the loop            
print("End of program")






