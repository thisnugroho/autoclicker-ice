#!/usr/bin/env python3

import pyautogui, sys, os
import time

# to do next 
# try to put value on x,y and x1, y1
# try the app

#------------------------------------

# setup
# x = some number
# y = some number
# if there is any place
# x1 = some number
# y1 = some number
# delay = some number
# repeat = ? 

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
        pyautogui.click(x, y)

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
            pass

if __name__ == '__main__':
    main()
