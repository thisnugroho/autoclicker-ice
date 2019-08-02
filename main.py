#!/usr/bin/env python3

import pyautogui, sys, os
import time
from pynput.keyboard import *
########################################
# Auto Clicker with Coordinates by Ice #
########################################


#------------------------------------
# Setup
# =================================
# Position 1
x = 588
y = 331
# if there is any Position
x1 = 793
y1 = 338
# Just add some  x2,y2, . . .
# if there is more than 1 position
# Time Delay                         
delay = 0.1                     
# Set Shortcut                  
p = Key.f4 # Pause              
r = Key.f2 # Resume             
s = Key.esc # Exit / Stop       
# ===============================

pause = True
running = True

def cekPosisi():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
            print('Bye')
            exit(0)

def auto(x, y):
        pyautogui.click(x = x, y = y)

def autoSingle():
        pyautogui.click()

def on_press(key):
        global running, pause

        if key == r:
                pause = False
                print('Resumed')
        elif key == p:
                pause = True
                print('Paused')
        elif key == s:
                running = False
                exit(0)


def main():
    print('\n')
    print('Press Ctrl-C to quit.')
    print('#####################')
    print('Ice Auto Clicker Tools')
    print('#####################')
    print("""
    1.Check Coordinates
    2.Auto Clicker (Multiple Position)
    3.Auto Clicker Normal (Current Pointer Position)
    """)
    opsi = input("Input : ")
    if opsi == '1':
        os.system('clear')
        cekPosisi()

    elif opsi == '2':
            print('Please Press F2 to start . . .')
        #     Add Listener to get keyboard Pressed
            lis = Listener(on_press=on_press)
            lis.start()
            while running:
                    if not pause:
                        #     Running The Auto Clicker
                            auto(x, y)
                            auto(x1, y1)
                            pyautogui.PAUSE = delay
            lis.stop()
            print('See Ya !')
    elif opsi == '3':
            print('Please Press F2 to start . . .')
        #     Add Listener to get keyboard Pressed
            lis = Listener(on_press=on_press)
            lis.start()
            while running:
                    if not pause:
                        #     Running The Auto Clicker
                            autoSingle()
                            pyautogui.PAUSE = delay
            lis.stop()
            print('See Ya !')

    else:
            print('Sorry,Wrong Input')

if __name__ == '__main__':
        try:
                main()
        except KeyboardInterrupt:
                print('\nBye')
