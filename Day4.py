# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 4 : 25-05-2020
# Day 4 | IG : https://www.instagram.com/benjivrik/
# Subject :  List
#----------------------------------------------------
# what would be the output of this program ?

'''

    use the function from Day 3 to insert the double of the parameter into
    a list five times  and return the list

'''

def double_parameter( value ):
    '''

        returning a list

    '''

    iteration = 0   #iteration param

    data  =  list() #initializing a list

    
    while(iteration < 5):  #This loop will stop when it reaches 5
        
        #Inside the loop
        
        data.append(value*2) #add a value

        #increases the loop
        iteration = iteration + 1
    
    return data



#main program



user_input  = input("Enter a number : ")  #line1

user_input  = int(user_input)             #line2

your_list = double_parameter(user_input)

print("Here is your list :  ", your_list)       #line3

#remove one element
your_list.pop()                                 #line4
 
print("Here is your new list :  ", your_list)       #line5


#insert 87 element at index 2

your_list.insert(2, 87)

print("Here is your new list with 87 :  ", your_list)       #line6


print("End of program")

