# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 17 :  7-06-2020
# Day 17 | IG : https://www.instagram.com/benjivrik/
# Subject :  Challenge VI - Writing in a File
#----------------------------------------------------
# what would be the output of this program ?

'''

    Use the program from Day16. 

    Look for all h5 in a specific and write them all in text file.

    Split them it two columns as shown below :

    Tag parsed = your_tag

    Tag Id    Tag Content
    ------    -----------
      1       Lorem ipsum
      2       Lorem ipsum


    The separators between your columns should be a tab '\t'
    ...
    
    where the Lorem ipsum have to be replaced by your tag content.
    and your_tag should be replaced by the tag your a look for.

    I will use the same url as Day16 -  'Terms and conditions'

    url = 'https://www.stuntbusiness.ca/fr/legal/terms-and-conditions'

'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

if not os.path.exists('text_data'):
    # if the folder does not exist create the folder 
    os.makedirs('text_data')



url = 'https://www.stuntbusiness.ca/fr/legal/terms-and-conditions'

content = urlopen(url)


#get the parser
parser =  BeautifulSoup(content, 'html.parser')

tag_id = 1 # for a convenient display,  the printing will have tags numbered
#html tag
tag_to_look_for = 'h5'

#open and write inside the file
    
your_file = open('text_data/day_17_data', 'w')

your_file.write("Tag parsed = {}".format(tag_to_look_for))

your_file.write("\nTags Id\t\tTags Contents")



print("Printing all {} found in the requested url {} \n".format(tag_to_look_for, url) )
#printing the tags
for tag in parser.find_all(tag_to_look_for) :
    
    your_file.write("\n{}\t\t{}".format(tag_id,tag))
    print( 'Tag {} : {}'.format(tag_id, tag))

    tag_id = tag_id + 1

your_file.close() # close your file

#open and read the file
    
your_file = open('text_data/day_17_data', 'r')

print("\n----------- READING ------------\n")

for line in your_file:
    print(line)



print("\nEnd of program")
