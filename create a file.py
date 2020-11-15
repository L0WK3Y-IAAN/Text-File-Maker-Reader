#!/usr/bin/python
# Goal of the script:
# 1. Get user input for directory (ex: "C:\" OR "/home/example/" ) (Windows or Linux)
# 2. Create a file called "test.txt" in the user's desired directory and write "test" inside the file.
#
# OR
#
# 1. Create a file called "test.txt" in the current directory and write "test" inside the file.
# 2. Get user input for directory (ex: "C:\" OR "/home/example/" ) (Windows or Linux)
# 3. Check if the directory existed or not;
#       if not:
#       Create the directory
#       If existed:
#       proceed to the next code
# 4. Move the "test.txt" file to desired directory

import sys
import subprocess
import os
import time

#Tries importing the required module if there is an ImportError, install python3-tk
try:
    import tkinter
except ImportError as error:

    #If system OS is linux perform actions below
    if sys.platform.startswith('linux'):

        #clears terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[+]Installing Tkinter...')

        #Installs tkinter package
        subprocess.call(['sudo apt-get install python3-tk'],shell=True)
        os.system('cls' if os.name == 'nt' else 'clear')

        #A restart is required for tkinter to work, allows user to restart now or later
        selection = input('[+]In order for Tkinter to work you must restart your system. Would you like to restart now or later?\n\n[y]= Yes.\n[n]= I will restart later.\n\n\nSelection: ')

        #Restart later
        if selection == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Exiting program...')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

        #Restart now
        elif selection == 'y':
            os.system('reboot')
        





#Uses tkinter GUI library to allow user to select their save path
from tkinter import *
from tkinter import filedialog



#Initialize tkinter 
root = Tk()

#Tkinter window title 
root.title('Select save directory')

#Uses the "askdirectory" function in the "filedialog" module imported from tkinter
root = filedialog.askdirectory()

#If the file directory has a space in it, perform the action below.
if ' ' in root:
    #Encases the directory into single quotes using string formatting
    dir = "'%s'" % root

    #Prints new formatted directory 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Path selected: ',dir)

    #Writes file to directory
    save_file = open('test.txt', 'w')
    save_file.write('test')
    save_file.close()

    #Reads file from directory and prints it to the terminal
    read_file = open('test.txt', 'r').read()
    print('\nFile contents:\n_________________\n\n' + read_file)

else:
    #Performs same actions as above but for directories that do not contain spaces.
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Path selected: ',root)
    save_file = open('test.txt', 'w')
    save_file.write('test')
    save_file.close()

    read_file = open('test.txt', 'r').read()
    print('\nFile contents:\n_________________\n\n' + read_file)