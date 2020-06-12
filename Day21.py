# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 21 : 11-06-2020
# Day 21 | IG : https://www.instagram.com/benjivrik/
# Subject : OOP - Inheritance
#----------------------------------------------------
# what would be the output of this program ?

'''

    You do not have to rewrite the same property for three differents 
    objects that have similarities.
    
    For example,

        Students and Teachers are Humans. 
    
    That could mean that the object Student will have the properties of a Human.
    This is the case for the Humans.


    So, the object Student 'inherits' the properties of a Human. Again, this will
    be the case for a Teacher.

    Student is the Child class, and Human is the Parent Class.
    How do you apply inheritance ?

        class ChildClassName(ParentClassName):
            ...

'''


class Human:
    # parent class
    def __init__(self,name,eye_color):
        self.name = name
        self.eye_color = eye_color
        self.must_eat = True
        

class Student(Human):
    # child class
    def __init__(self, name, eye_color,student_id,year_level):
        super().__init__(name, eye_color)
        self.student_id =  student_id
        self.year_level =  year_level
        self.address = ""

    # set address
    def set_address(self,address):
        self.address = address


class Teacher(Human):
    # child class
    def __init__(self, name, eye_color, teacher_id, teacher_class):
        super().__init__(name, eye_color)
        self.teacher_id = teacher_id
        self.teacher_class = teacher_class
        self.office_number = 0
        
    # set office
    def set_office(self, office_number):
        self.office_number = office_number
    


if __name__ == "__main__" :
    h = Human("Tim","Brown")
    print("Getting property must_eat for Human :",h.must_eat )
    s = Student("Student-1","Brown","11152","4")
    print("Getting property must_eat for Student :",s.must_eat )
    t = Teacher("Teacher-1","Brown","11152","IT")
    print("Getting property must_eat for Teacher :",t.must_eat )

    t.set_office(540)
    print("Getting the office_number from the teacher object :", t.office_number)

    # The following line will throw an error ...
    # ... since the office_number does not exist in Human.
    # Since the must_eat is a property of the Parent Class Human ...
    # ... the children inherit the property must_eat
    # But the Parent does not have access to the Child properties

    try:
        print("Getting the office_number from the human object :", h.office_number)
    except AttributeError :
        print("Caused by the Error Attribute Error.  The Human class does not have the attribute office_number")

    print("End of program")



