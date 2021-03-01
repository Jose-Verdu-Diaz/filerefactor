import os, sys
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

dir = filedialog.askdirectory()

try:
    leadingNum = int(input('Enter leading number:'))
except ValueError:
    sys.exit("Program stopped. Error: The input was not a number")

try:
    firstNum = int(input('Enter first file number:'))
except ValueError:
    sys.exit("Program stopped. Error: The input was not a number")

reverse = input("Reverse order? (y) (No by default)") == 'y'



if os.path.isdir(dir):
    for i, filename in enumerate(sorted(os.listdir(dir) , reverse = reverse)):
        os.rename(dir + "/" + filename, dir + "/" + str(leadingNum).zfill(4) + '-' + str(i + firstNum).zfill(4))
