import os
from tkinter import *
import subprocess as sub

p = sub.Popen(['sample.py'],shell=True)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()