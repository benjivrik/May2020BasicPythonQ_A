# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 19 : 9-06-2020
# Day 19 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge VIII Data processing - Read and Plot
#----------------------------------------------------
# what would be the output of this program ?

'''

    A bit of math.  This will be related to plotting
    data received from a file.

    Open a text file and write inside the following content:

    Angle  Cosine  Sine
    0
    15
    30
    45
    60
    75
    ...

    Generate your angle from 0 to 360. 
    And add a 15 degrees span between each angle value.

    
    Close the File.

    Read the File you have just created.

    and using the matplotlib.pyplot module, 
    plot the cosine and sine values 
    with two different graphs.

    The module numpy will help you to generate the required values
    for your array.

    Use its function arange(start,stop,step) where step should be 15
    in our case.

    Use the module math for the sine and cosine calculations.

'''
import numpy as np 
import math
import matplotlib.pyplot as plt
import re


# generate data

# 195 won't be added in the array
# data from 0 to 180
data = np.arange(0,375,15) 

# open and write inside the file
    
your_file = open('text_data/day_19_data', 'w')

your_file.write("Angle\t\tCosine\t\tSine")

#printing the tags
for angle in data:
    # convert to radians
    angle_rad = np.radians(angle)
    # sine value
    sine = math.sin(angle_rad)
    # cosine value
    cosine = math.cos(angle_rad)
    # write inside the file
    your_file.write("\n{}\t\t{}\t\t{}".format(angle,cosine,sine))

#close the file
your_file.close()

# read the content of the file

your_file = open('text_data/day_19_data', 'r')

#list for values

angle_values = list()
cosine_values = list()
sine_values = list()

for line in your_file :
    # split on the tabs
    
    data = line.strip('\n')
    data = data.split('\t')

    # clear empty elements
    data = [word for word in data if word]

    # # This block is for clearing the new line character in the 'word'
    # # Suggest a better approach
    # for word in data:
    #     if '\n' in word:
    #         # find the index of the '\' character
    #         remove_index = word.index('\n')
    #         # find the index of the word with the new line character
    #         word_index = data.index(word)
    #         # replace the element with the new element
    #         data[word_index] = word[0:remove_index]
        

    
    # get the values
    # the only string should come from the first line
    if not data[0].isalpha() and data[0].isdigit():
       # angles
       angle_values.append(float(data[0]))
       # cosine values
       cosine_values.append(float(data[1]))
       # sine values
       sine_values.append(float(data[2]))


your_file.close()

#plotting values.

plt.plot(angle_values, sine_values,angle_values, cosine_values)
plt.legend(['sin(angle)', 'cos(angle)'])  
plt.title("Cosine an Sine Plot")
plt.ylabel("cos(angle) and sin(angle)")
plt.xlabel("Angles (deg)")
plt.grid()
plt.show()



