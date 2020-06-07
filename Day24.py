# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 20 : 14-06-2020
# Day 20 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge XI - Create a File Manager using OOP
#----------------------------------------------------
# what would be the output of this program ?

'''
    Create a file manager using OOP.

    Let the object you create allow you to write and read the
    files stored in a specific folder.

    When you create your instance, let the user enter the folder and the file name
    he wants to work on.

    Create a function for writing inside a file (appending a content inside a file),
    and for reading the file stored in that folder.

    Work with a .txt file for now.

'''
import os

class FileManager :
    # instantiate the class
    def __init__(self, folder_path, filename):
        '''
            str - folder path : 'path'
            str - filename : 'text.txt' for example
        '''
        # initialize the folder you work on
        self.__folder_path =  folder_path
        # if the folder does not exist, create it.
        if not os.path.exists(self.__folder_path):
            # if the folder does not exist create the folder 
            os.makedirs(self.__folder_path)
        # file name 
        self.__filename = filename
        # complete path
        self.__path = self.__folder_path + "/" + self.__filename
        #initialize empty file
        open(self.__path,'w').close()

    #set a new file to work on
    def set_filename(self, filename):
        # change the filename
        self.__filename = filename
        print("New file name set successfully.\nNew file name : {}.\n".format(self.__filename))
        # update path
        self.__path = self.__folder_path + "/" + self.__filename
        # initialize empty path
        open(self.__path,'w').close()

    #get a new file to work on
    def get_filename(self):
        # change the filename
        return self.__filename
    
    #set a new folder you want to work on
    def set_folder_path(self, folder_path):
        # change the filename
        self.__folder_path = folder_path
        # create the folder if it does not exist
        if not os.path.exists(self.__folder_path):
            # if the folder does not exist create the folder 
            os.makedirs(self.__folder_path)
        print("New folder set successfully.\nNew folder name : {}.\n".format(self.__folder_path))
        # update path
        self.__path = self.__folder_path + "/" + self.__filename
        # initialize empty path
        open(self.__path,'w').close()

    #get a new file to work on
    def get_folder_path(self):
        # change the filename
        return self.__folder_path
    
    #append a content to the existing content in files
    def add_content_in_file(self, data):
        # use the mode append 'a'
        your_file = open(self.__path, 'a')
        your_file.write(data)
        your_file.close()

    #display the content in all the file
    def display_all_data(self):
        your_file = open(self.__path,'r')
        for line in your_file :
            print(line)
        your_file.close()

    # str representation of your object
    def __str__(self):
        env =  "\nHello, your current folder is '{}/'.\n".format(self.__folder_path)
        env = env + "And you are working with the file '{}'.\n".format(self.__filename)
        env = env + "Your full path is : '{}'.\n".format(self.__path)
        return env


if __name__ == "__main__":
    file_manager =  FileManager('text_data','day_24_data.txt')
    print(file_manager)

    print("\n-------- ADDING TEXT --------\n")
    print("Adding 'Day-24 blah blah', 'TEST' and 'blah blah blah'.")
    # adding random data
    file_manager.add_content_in_file("blah blah\n")
    file_manager.add_content_in_file("TEST\n")
    file_manager.add_content_in_file("blah blah blah\n")

    print("\n-------- READING --------\n")
    file_manager.display_all_data()

    print("\n-------- CHANGING FILE NAME --------\n")
    print(file_manager)

    # changing file
    file_manager.set_filename('data_24_data_bis.txt')
    #changing folder
    file_manager.set_folder_path('text_data_bis')

    print("\n-------- READING THE NEW FILE--------\n")
    file_manager.display_all_data()

    print("\n-------- ADDING TEXT IN THE NEW FILE --------\n")
    print("Adding 'Day-24 blah blah', 'TEST' and 'blah blah blah'.")
    # adding random data
    file_manager.add_content_in_file("Day-24\nblah blah\n")
    file_manager.add_content_in_file("TEST\n")
    file_manager.add_content_in_file("blah blah blah\n")

    print("\n-------- READING THE NEW FILE--------\n")
    file_manager.display_all_data()

    print("End of program")