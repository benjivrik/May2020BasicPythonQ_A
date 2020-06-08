# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 20 : 12-06-2020
# Day 20 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge IX - Create a calculator using OOP
#----------------------------------------------------
# what would be the output of this program ?

'''

    Take the same basic calculator concept from Day7.

    Create your class Calculator in which you can add all 
    your required functions : sum, subtract, mutiply and
    divide.

    You do not need to pass the operands when 
    creating the instance Calculator.

    Add a  method display_all_result(a,b) that will print
    the result of all the functions for the operands a and b.

'''

class Calculator:

    def __init__(self):
        print("Calculator created.")
    
    # add
    def add_operands(self,a,b):

        '''
            a+b
        '''
        return a + b


    # substract
    def subtract_operands(self,a,b):

        '''
            a-b
        '''
        return a-b

    # divide
    def divide_operands(self,a,b):
        
        '''
            a/b
        '''

        if(b == 0): #can not divide by zero
            print("You can not divide a number by 0")
            while(b==0):
                b = float(input("enter a correct value for b different from zero:"))

        return a/b

    # multiply
    def multiply_operands(self,a,b):
        '''
            a*b
        '''
        return a*b
    
    def display_all_result(self,a,b):
        '''
            Display all the result
        '''
        addition = "{} + {} = {}\n".format(a,b,self.add_operands(a,b))
        subtraction = "{} + {} = {}\n".format(a,b,self.subtract_operands(a,b))
        division = "{} + {} = {}\n".format(a,b,self.divide_operands(a,b))
        multiplication = "{} + {} = {}\n".format(a,b,self.multiply_operands(a,b))
        print(addition + subtraction + division + multiplication)
        return "Executed. End of display_all_result "


if __name__ == "__main__":
    # main program
    calc = Calculator()
    # randomly choosen calculation
    print("Executing calculation for a = 5 and b = 6")
    print("5 + 6 = {}".format(calc.add_operands(5,6)))
    print("5 - 6 = {}".format(calc.subtract_operands(5,6)))
    print("5 / 6 = {}".format(calc.divide_operands(5,6)))
    print("5 * 6 = {}".format(calc.multiply_operands(5,6)))

    print("\nExecuting calculation for a = 5 and b = 6 using display_all_result")
    print(calc.display_all_result(5,6))
    print("\nEnd of Program")

