# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 18 : 8-06-2020
# Day 18 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge VII - Read, Copy and Print
#----------------------------------------------------
# what would be the output of this program ?


'''

    Use the same text file from from Day17. 

    Read the file,

    Create a new file for Day18

    Copy the content of the original file Day17 inside the file for Day18

    Read the file for Day18

    Look for all even ids only first and print them.

    Read the file again

    Then Look for all odd ids only and print them.


'''


print("\n----------- READING & COPYING ------------\n")

old_file =  open('text_data/day_17_data', 'r')

new_file = open('text_data/day_18_data', 'w')

# reading and copying content

for line in old_file:
    new_file.write(line)

# close the files
old_file.close()
new_file.close()

print("\n----------- PARSING THE NEW FILE ------------\n")

#empty dictionaries
even_lines = {}
odd_lines = {}

# open the new file again

new_file = open('text_data/day_18_data', 'r')


for line in new_file :

    data  = line.split('\t') # splitting data on the tab

    # removing empty elements in data
    # if elem executes only if the elem is not empty

    data = [elem for elem in data if elem]

    #if the first element is not a number you did not reach the ids part in your file

    if not data[0].isalpha() and data[0].isdigit() :
        # a number is even when rest of division by 2 is zero
        # odd when the rest of the division is not zero
        if ( int(data[0]) % 2 == 0 ) :
            # add the element in the dictionary
            # id > content
            even_lines[data[0]] = data[1]
        else :
            odd_lines[data[0]] = data[1]
    



print("\n----------- PRINTING EVEN ROWS ------------\n")
# display even rows

for id in even_lines:
  print("Row id > {} | \nRow content: {}".format(id,even_lines[id]))

# display odd rows

print("\n----------- PRINTING ODD ROWS ------------\n")

for id in odd_lines:
  print("Row id > {} | \nRow content: {}".format(id,odd_lines[id]))


new_file.close()
print("\nEnd of Program\n")

        


    




