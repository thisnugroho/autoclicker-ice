#!/usr/bin/env python3

import pyautogui, sys, os
import time
from pynput.keyboard import *

# to do next 
# try to put value on x,y and x1, y1
# try the app

#------------------------------------
# Setup
# =================================
# Position 1
x = 588
y = 331
# if there is any Position
x1 = 793
y1 = 338
# Delay
delay = 0.5
# Set Shortcut
p = Key.f1 # Pause
r = Key.f2 # Resume
s = Key.esc # Exit / Stop
# ===============================

pause = False
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
            print('\n')

def auto(x, y):
        pyautogui.click(x = x, y = y)

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
    print('Ice Auto Clicker Tools')
    print('----------------------')
    print("""
    1.Cek Posisi
    2.Auto
    """)
    opsi = input("Input : ")
    if opsi == '1':
        os.system('clear')
        cekPosisi()

    elif opsi == '2':
            lis = Listener(on_press=on_press)
            lis.start()
            while running:
                    if not pause:
                            auto(x, y)
                            auto(x1, y1)
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
