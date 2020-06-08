# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 20 : 10-06-2020
# Day 20 | IG : https://www.instagram.com/benjivrik/
# Subject : Object Oriented Programming
#----------------------------------------------------
# what would be the output of this program ?

'''
    
    What is Object Oriented Programming (OOP) ?

    Internet > Solving problems by creating objects.

    I compare these objects to boxes in which you add all the 
    properties necessary to describe  a unique component.

    For example, your university would need students, or teachers.
    And students and teachers would need ids and names.

    Let's create a simple class Human.  A human has a name, an age
    and what else ? Add whatever you want for now.

    From there, create two instances of the class Human.

    In a class, you have a 'constructor' which is a method defined in your
    class for initializing all the properties inside your object.

'''

class Human:
    # constructor
    def __init__(self, name, age, eye_color):
        self.name = name
        self.age = 34
        self.eye_color = eye_color
    # get the name of the Human
    def get_name(self):
        return self.name

    # set the name of the Human
    def set_name(self, name):
        self.name = name
    
    # get the age of the Human
    def get_age(self):
        return self.age

    # get the name of the Human
    def get_eye_color(self):
        return self.eye_color
    

if __name__ == "__main__" :
    
    human1 = Human('Test_One', 34, "brown")
    human2 = Human('Test_Two', 25, "Blue")

    # getting the age of each human

    print("> Age for human 1 using get_age(): ", human1.get_age())
    print("> Age for human 2 not using get_age():", human2.age)

    # changing the name of each human

    print("> Changing the name for human 2 using set_name().")
    human2.set_name("Tim")
    print("Done")
    print("> Changing the name for human 1 not using set_name().")
    human1.name="Bob"
    print("Done")

    # printing the name of the people 

    print("> Printing the name for human 2 using get_name() : ", human2.get_name())

    print("> Printing the name for human 1 using get_name(): ", human1.name)

        