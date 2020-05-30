# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 11 : 31-05-2020
# Day 11 | IG : https://www.instagram.com/benjivrik/
# Subject : File Handling
#----------------------------------------------------
# what would be the output of this program ?

'''

    Basic User-file Interaction.

    * Let's first open a file, append this text inside
    
    "
        Hello, I am a test.
        Append a text at the end of the file.
    "

    * Close the file

    * Print the content of the file

    * Close the file

    * Append this text inside your file.

    "

        Added!

    "

    * When this is done,

    * Open the same file again, read the content,and print it.



    > I am adding the file in the folder 'text_data', and my
    text file name is day_11_data

    * Use the function open(filename,mode)

    * The  mode 'w' will create the file
      if it does not exists and allows you
      to write inside the element but will clear
      the existing content.

    * The mode 'a' will append the text you are trying to
      add after the existing content.

    * Use 'r' for reading the content of your file

'''



import os  #module for using your Operating System functionalities

if not os.path.exists('text_data'):
    # if the folder does not exist create the folder 
    os.makedirs('text_data')

#open and write inside the file
    
your_file = open('text_data/day_11_data', 'w')

your_file.write("Hello, I am a test.\nAppend a text at the end of the file.")

your_file.close()

print("\n----------- READING ------------\n")
#open and read the file

your_file =  open('text_data/day_11_data', 'r')

#print the content of your file

print(your_file.read())

your_file.close()

print("\n----------- ADDING TEXT ------------\n")

#open and append the text inside the file

your_file = open('text_data/day_11_data', 'a')

your_file.write("\nAdded!")

your_file.close()

print("\n----------- READING ------------\n")

#open and read the file

your_file =  open('text_data/day_11_data', 'r')

#print the content of your file

print(your_file.read())

your_file.close()

print("\n----------- END OF PROGRAM ------------\n")








