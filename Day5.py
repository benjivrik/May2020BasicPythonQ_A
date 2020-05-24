# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 5 : 26-05-2020
# Day 5 | IG : https://www.instagram.com/benjivrik/
# Subject : Reusability > Parameterize your functions | Split them in blocks
#----------------------------------------------------
# what would be the output of this program ?

'''

    use the function from Day 3 to insert the double of the parameter into
    a list five times  and return the list

'''

def double_parameter(value, size):
    '''
        - value : int
        - size : size of list

        returning a list

    '''

    iteration = 0   #iteration param

    data  =  list() #initializing a list
    
    while(iteration < size):  #This loop will stop when it reaches 5
        
        #Inside the loop
        
        data.append(value*2) #add a value

        #increases the loop
        iteration = iteration + 1
    
    return data



def operation_on_list(your_list):

    '''
        your_list is the list passed as parameter
    '''

    print("Here is your list :  ", your_list)             #line6
    #remove one element
    your_list.pop()                                       #line7
    print("Here is your new list :  ", your_list)         #line8
    #insert 87 element at index 1
    your_list.insert(0, 87)
    print("Here is your new list with 87 :  ", your_list)       #line9


#main program


stop = 'no'


while stop == 'no' :  #this is a loop with a condition

    user_input  = input("Enter a number : ")  #line1
    user_input  = int(user_input)             #line2
    list_size   = input("Enter the size of your list : ") #line3
    list_size   = int(list_size)              #line4
    your_list   = double_parameter(user_input, list_size) #line5
    
    #your_list
    operation_on_list(your_list)

    #ask the user if he wants to contine
    stop = input("Do you wanna stop ? yes or no : ") #line10
    if(stop != "yes"):
        stop = "no"
    else :
        break #stop the loop


#outside_the_loop            
print("End of program")

