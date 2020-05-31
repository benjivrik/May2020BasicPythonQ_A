# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 13 : 3-06-2020
# Day 13 | IG : https://www.instagram.com/benjivrik/
# Subject : Time and Calendar
#----------------------------------------------------
# what would be the output of this program ?

'''

    You can have access to the date and time in your  code
    using the module calendar, time, or datetime. I may be
    missing something here.

    You may want to execute a specific action at a specific time
    in your program.

    You may also want to measure the time of execution of your code.

    The timestamp matters in your program if you want to evaluate 
    the execution speed  for different programming approaches.

    Let's evaluate the execution time from a section I to a section II
    in your code.

'''

import calendar
import time



your_time_in_millis_first = int(time.time()*1000)

print("\n I - Get Calendar Data \n ")

your_calendar = calendar.TextCalendar(2020)

# Printing  February
print(your_calendar.formatmonth(2020,2))

print("-----------------")

# Printing December
print(your_calendar.formatmonth(2020,12))

print("----------------")

your_calendar = calendar.calendar(2020)
# Printing the full year calendar
print(your_calendar)

print("\n II - Months and Year printed above. \n ")

your_time_in_millis_second = int(time.time()*1000)

diff = your_time_in_millis_second - your_time_in_millis_first

print("It tooks  {} ms to execute from I to II. ".format(diff))




