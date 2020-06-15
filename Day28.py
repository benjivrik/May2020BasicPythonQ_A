# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 28 : 18-06-2020
# Day 28 | IG : https://www.instagram.com/benjivrik/
# Subject : GUI - tkinter
#----------------------------------------------------
# what would be the output of this program ?

'''

    Your app is not eternally stick to a terminal.

    Python allows you to create GUI ( Graphical User Interface ).

    The module tkinter can be used for that.

    Let's create our first GUI with an image, text and entries and a submit button.
    
'''

import tkinter as tk

# initialize your tkinter object
window = tk.Tk()
window.resizable(False,False)
window.geometry("600x480")
window.title("First GUI.")

# create frame
frame = tk.Frame(window, width=600, height=300, background="white")
frame.pack(side=tk.TOP)

# create frame bottom
frame_bottom = tk.Frame(window, width=600, height=100, background="white")
frame_bottom.pack(side= tk.TOP)

canvas = tk.Canvas(frame, width=200,height=300, bg="white",bd=1, highlightthickness=0,relief="solid")
canvas.pack(side=tk.LEFT,fill='both', expand='yes',padx=5,pady=5)

img = tk.PhotoImage(file="img_data/android-chrome-192x192.png")
canvas.create_image(100, 150, anchor=tk.CENTER, image=img)
#right canvas
canvas_right = tk.Canvas(frame, width=400,height=300, bd=1, highlightthickness=0,relief="solid")
canvas_right.pack(side=tk.RIGHT ,fill=tk.BOTH, expand='yes',padx=5,pady=5)


# text canvas
text = '''
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Curabitur venenatis purus vel\n
lectus sollicitudin bibendum. 
'''
canvas_right.create_text(200,150,fill="black", font="Times 15 bold",
                        text=text, anchor=tk.CENTER)

#bottom canvas
canvas_right = tk.Canvas(window, width=600, height=300, bd=1, highlightthickness=0,relief="solid")
canvas_right.pack(side=tk.BOTTOM ,fill='both', expand='yes')


# add entries in the bottom frame

canvas_frame_bottom = tk.Canvas(frame_bottom, width=600, height=100, bd=1, highlightthickness=0,relief="solid")
canvas_frame_bottom.pack(fill='both',expand='yes')

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

submit = tk.Button(canvas_frame_bottom, text="Submit",width=200,height=15,relief=tk.GROOVE)
submit.pack()

# window
window.mainloop()