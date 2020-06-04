# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 14 : 4-06-2020
# Day 14 | IG : https://www.instagram.com/benjivrik/
# Subject : Module - Matplotlib.pyplot
#----------------------------------------------------
# what would be the output of this program ?

'''

    It is possible to graphically vizualise any set 
    of data ('graphically visualizable') in your program.

    The module matplotlib.pyplot allows you to visualize your data 
    through graphs.

    Let's collect five values of the execution speed between blocks in our
    program as previously shown in Day 13 and plot the collected values.

    The result is meaningless for now.
    Take the time to analyze the available functions.

'''

import matplotlib.pyplot as plt
import time



your_I = int(time.time()*1000)

print("BLOCK I_to_II")
print("Adding a random line.")

your_II = int(time.time()*1000)

print("BLOCK II_to_III")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")

your_III = int(time.time()*1000)

print("BLOCK III_to_IV")
print("Adding a random line.")
print("Adding a random line.")

your_IV = int(time.time()*1000)


print("BLOCK IV_to_V")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")

your_V =  int(time.time()*1000)

print("BLOCK V_to_VI")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")


your_VI =  int(time.time()*1000)

print(
    "\n> Delay block I to II : {} ms".format(your_II - your_I),
    "\n> Delay block II to III : {} ms".format(your_III - your_II),
    "\n> Delay block III to IV : {} ms".format(your_IV - your_III),
    "\n> Delay block IV to V : {} ms".format(your_V - your_IV),
    "\n> Delay block V to VI : {} ms".format(your_VI - your_V)
)

data = list()
data.append(your_II - your_I)
data.append(your_III - your_II)
data.append(your_IV - your_III)
data.append(your_V - your_IV)
data.append(your_VI - your_V)

print("Your data : {}".format(data))

plt.plot(data, 'b--')
plt.ylabel('Time (ms)')
plt.axis([0,4,0,48])
plt.title('Block I-II, II-III, III-IV,IV-V, V-IV')
plt.grid()
plt.show()
