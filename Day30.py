# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 30 : 20-06-2020
# Day 30 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge XVI - Save data from entries in a text file using the File Manager
#----------------------------------------------------
# what would be the output of this program ?


'''

    Use the file Manager from Day24 and 
    write the data you read from the entries inside a text file.

    Add a field for the first name, the last name and the phone number.

    Take the code from the Day28 and add the File Manager.
    
'''

import tkinter as tk
import Day24

# initialize file manager
file_manager =  Day24.FileManager('text_data','day_30_data.txt')
print(file_manager)

count = 0
# get entries from the text
def get_entries():

    # variable count 
    global count
    count +=1

    print("\n-------- ADDING TEXT --------\n")
    file_manager.add_content_in_file("Count : {}\n\n--------\n".format(count))
    # adding random data
    file_manager.add_content_in_file("First Name : {}\n".format(entr_one_text.get()))
    file_manager.add_content_in_file("Last Name : {}\n".format(entr_two_text.get()))
    file_manager.add_content_in_file("Phone Number : {}\n\n------------\n".format(entr_third_text.get()))

    print("\n-------- READING --------\n")
    file_manager.display_all_data()

# initialize your tkinter object
window = tk.Tk()
window.resizable(False,False)
window.geometry("600x480")
window.title("First GUI.")

# create frame (top)
frame = tk.Frame(window, width=600, height=300, background="white")
frame.pack(side=tk.TOP)

# create frame bottom
frame_bottom = tk.Frame(window, width=600, height=100, background="white")
frame_bottom.pack(side= tk.BOTTOM)


# -----------------------
# TOP FRAME ELEMENTS
# -----------------------

# image container
canvas = tk.Canvas(frame, width=200,height=300, bg="white",bd=1, highlightthickness=0,relief="solid")
canvas.pack(side=tk.LEFT,fill='both', expand='yes',padx=5,pady=5)

img = tk.PhotoImage(file="img_data/android-chrome-192x192.png")
canvas.create_image(100, 150, anchor=tk.CENTER, image=img)

#right canvas
canvas_right = tk.Canvas(frame, width=400,height=300, bd=1, highlightthickness=0,relief="solid")
canvas_right.pack(side=tk.RIGHT ,fill=tk.BOTH, expand='yes',padx=5,pady=5)


# text canvas
text = '''
Write data from entries\n
inside a text file.
'''
canvas_right.create_text(200,150,fill="black", font="Times 15 bold",
                        text=text, anchor=tk.CENTER)



# -----------------------
# BOTTOM FRAME ELEMENTS
# -----------------------

# add entries in the bottom frame
canvas_frame_bottom = tk.Canvas(frame_bottom, width=600, height=100, bd=1, highlightthickness=0,relief="solid")
canvas_frame_bottom.pack(fill='both',expand='yes',padx=5,pady=2)

entr_one_text = tk.StringVar()
entr_one_text.set("Enter your first name")

entr_two_text = tk.StringVar()
entr_two_text.set("Enter your last name")

entr_third_text = tk.StringVar()
entr_third_text.set("Enter your phone number.")

# first entry
entry_one_label = tk.Label(canvas_frame_bottom, text="First name:", width=200,anchor=tk.W)
entry_one_label.pack()

entry_one = tk.Entry(canvas_frame_bottom, textvariable=entr_one_text, width =400)
entry_one.pack()

# second entry
entry_two_label = tk.Label(canvas_frame_bottom, text="Last name", width=200,anchor=tk.W)
entry_two_label.pack()

entry_two = tk.Entry(canvas_frame_bottom, textvariable=entr_two_text, width = 400)
entry_two.pack()

# third entry
entry_three_label = tk.Label(canvas_frame_bottom, text="Phone number", width=200,anchor=tk.W)
entry_three_label.pack()

entry_three = tk.Entry(canvas_frame_bottom, textvariable=entr_third_text, width =400)
entry_three.pack()

submit = tk.Button(canvas_frame_bottom, text="Submit",fg="white",bg="purple",width=200,height=15,relief=tk.GROOVE, command=get_entries)
submit.pack(pady=2)

# window
window.mainloop()


