# lightsOut.py: a program to solve the Lights Out game
# Copyright (C) 2015  Michael Silver

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# For a copy of the GNU General Public License, see LICENSE in the
# repository's root directory.

import numpy as np

def main():
    quit = False
    
    while(not quit):
        # get the button number from user
        buttonNumber = input("Enter your button number (-1 to quit): ")

        # if 'q' is entered, quit
        if(buttonNumber == -1):
            print("quitting...")
            quit = True
        elif(buttonNumber > -1 and buttonNumber < 25):
            # check all the edge cases
            if(not buttonNumber < 5):
                print(buttonNumber-5)

            if(not buttonNumber > 19):
                print(buttonNumber+5)

            if(buttonNumber % 5 != 0):
                print(buttonNumber-1)

            if(buttonNumber % 5 != 4):
                print(buttonNumber+1)
        else:
             print("Please enter a number between 0 and 24")
        
main()                          # call the main function

## reference of 5x5 grid:

# 0  1  2  3  4 
# 5  6  7  8  9 
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24
