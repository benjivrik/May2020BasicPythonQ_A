# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 6 : 27-05-2020
# Day 6 | IG : https://www.instagram.com/benjivrik/
# Subject : conditions and boolean
#----------------------------------------------------
# what would be the output of this program ?

'''

    if( condition ) :
    
        when this condition  is True, this block executes
        
    elif( condition ) :
    
        when the previous condition is not executed
        if this condition is True, this block executes
        
    else :

        if none of the above conditions are satisfied, this
        block executes


    type(True) return <class 'bool'>

    True or False are booleans.
'''

def double_parameter(value):

    '''
        parameter value - float
        return data * 2
    '''
    
    return value * 2



def divide_parameter_by_two(value):

    '''
        parameter value - float
        return data * 2
    '''
    
    return value / 2

def add_two_to_parameter(value):
    
    '''
        parameter value - float
        return data + 2
    '''

    return value + 2
    


#main program

stop = "no"



while stop == 'no' :  #this is a loop with a condition
    
    user_input = input("Enter a value : ")
    user_input = float(user_input)

    if( user_input < 5 ) :
        #add two to parameter
        print("Adding 2 : ", add_two_to_parameter(user_input))

    elif(user_input >= 5 and user_input < 10 ):
        #divide
        print("Dividing by 2 : " , divide_parameter_by_two(user_input))

    else :    #if the value is >= 10
        print("Multiplying by 2 : " , double_parameter(user_input))

   #ask the user if he wants to contine
    stop = input("Do you wanna stop ? yes or no : ") #line10
    if(stop != "yes"):
        stop = "no"
    else :
        break #stop the loop    


#outside_the_loop            
print("End of program")

