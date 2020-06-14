# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 20 : 18-06-2020
# Day 20 | IG : https://www.instagram.com/benjivrik/
# Subject : GUI - tkinter
#----------------------------------------------------
# what would be the output of this program ?

'''

    Your app is not eternally stick to a terminal.

    Python allows you to create GUI ( Graphical User Interface ).

    The module tkinter can be used for that.

    Let create our first GUI with an image, text and entries.
    

'''

import tkinter as tk

# initialize your tkinter object
window = tk.Tk()
window.resizable(False,False)
window.geometry("600x500")

# create frame
frame = tk.Frame(window, width=600, height=300, background="gray")
frame.pack(side=tk.TOP)

# create frame bottom
frame_bottom = tk.Frame(window, width=600, height=300,bd=2, background="yellow",relief=tk.SOLID)
frame_bottom.pack(side= tk.BOTTOM)

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
canvas_right.create_text(0,0,fill="darkblue",font="Times 20 italic bold",
                        text=text, anchor=tk.NW)

#bottom canvas
canvas_right = tk.Canvas(window, width=600, height=300, bd=1, highlightthickness=0,relief="solid")
canvas_right.pack(side=tk.BOTTOM ,fill='both', expand='yes')


# window
window.mainloop()