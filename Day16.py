# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 16 : 6-06-2020
# Day 16 | IG : https://www.instagram.com/benjivrik/
# Subject : Web scraping with python
#----------------------------------------------------
# what would be the output of this program ?


'''

    You can access the content from a specificied url in python and
    process the information you download in your program. 

    The modules used here are urllib2 and BeautifulSoup.

    * Internet definitions following

    + urllib2 > a module that allows you to open URLs. 

    + BeautifulSoup > a module that allows you to extract data from HTML and XML files. 
    
    Let's extract the data from the group webpage 'Terms and Conditions';

    link : https://www.stuntbusiness.ca/fr/legal/terms-and-conditions

    Let's get all the HTML h4 tags on this page and print them in the terminal.

'''


from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.stuntbusiness.ca/fr/legal/terms-and-conditions'

content = urlopen(url)

#full html tags will be displayed on your terminal if you remove the comment hashtag for the next line
#print(content.read())

#get the parser
parser =  BeautifulSoup(content, 'html.parser')

tag_id = 1 # for a convenient display,  the printing will have tags numbered
#html tag
tag_to_look_for = 'h4'

print("Printing all {} found in the requested url {} \n".format(tag_to_look_for, url) )
#printing the tags
for tag in parser.find_all('h4') :
    print( 'Tag {} : {}'.format(tag_id, tag))
    tag_id = tag_id + 1

print("\nEnd of program")