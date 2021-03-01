import os, sys
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

dir = filedialog.askdirectory()

try:
    patientNum = int(input('Enter patient number:'))
except ValueError:
    sys.exit("Program stopped. Error: The input was not a number")

try:
    firstNum = int(input('Enter first image number:'))
except ValueError:
    sys.exit("Program stopped. Error: The input was not a number")

try:
    reverse = input("Reverse order? (y) (No by default)") == 'y'
except ValueError:
    sys.exit("Program stopped. Error: The input was not a number")


if os.path.isdir(dir):
    for i, filename in enumerate(sorted(os.listdir(dir) , reverse = reverse)):
        os.rename(dir + "/" + filename, dir + "/" + str(patientNum).zfill(4) + '-' + str(i + firstNum).zfill(4))
