# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 7 : 28-05-2020
# Day 7 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenges II - Basic Calculator
#----------------------------------------------------
# what would be the output of this program ?

'''

    Create a basic calculator that let the user
    choose between the following operators
    +,-,*,/

    and let the user enter the operands a and b
    
'''

def add_operands(a,b):

    '''
        a+b
    '''
    return a + b



def substract_operands(a,b):

    '''
        a-b
    '''
    return a-b

def divide_operands(a,b):
    
    '''
        a/b
    '''

    if(b == 0): #can not divide by zero
        print("You can not divide a number by 0")
        while(b==0):
            b = float(input("enter a correct value for b different from zero:"))

    return a/b

def multiply_operands(a,b):
    '''
        a*b
    '''
    return a*b
    


#main program

stop = "no"

operators = ["+","-","*","/"]

while stop == 'no' :  #this is a loop with a condition

    #get the value for a
    a = input("Enter a value for a : ")
    
    if(a.isdigit()): #make sure that a is a digit
       a = float(a)
    else:
        while(~a.isdigit()):
            a = input("Enter a digit for a : ")
        a = float(a)

    #get the value for b
    b = input("Enter a value for b : ")
    
    if(b.isdigit()): #make sure that b is a digit
       b = float(b)
    else:
        while(~b.isdigit()):
            b = input("Enter a digit for a : ")
        b = float(b)


    #get the operators
    print("Available operators : ", operators)
    operator = input("Choose your operator : ")

    #make sure the user enter the correct operator
    while not operator in operators :
        operator = input("Choose a correct operator: ")

    if operator  == "+":
        print("a+b = ", add_operands(a,b))

    if operator == "-":
        print("a-b = ", substract_operands(a,b))

    if operator == "*":
        print("a*b = ",multiply_operands(a,b))

    if operator == "/" :
        print("a/b = ", divide_operands(a,b))
        
    

   #ask the user if he wants to contine
    stop = input("Do you wanna stop ? yes or no : ") #line10
    if(stop != "yes"):
        stop = "no"
    else :
        break #stop the loop    


#outside_the_loop            
print("End of program")

