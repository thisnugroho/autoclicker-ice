# Auto Clicker By Ice Using Python 
  

#### Screenshoot of the App

![Screenshoot App](http://imgur.com/ognAAYUl.png)

## Requirement
- You need install pyautogui first if you don't have it
````
pip install pyautogui
or
pip3 install pyautogui
```` 
## Feature And How to Use
1.  Check Coordinates

![Check Coordinates](http://imgur.com/0Ve8dLvl.png)

It's app that can know where is your mouse position
How to Use it :
	- first thing you do is to clone this repositories
	````
	git clone https://github.com/thisnugroho/autoclicker-ice
	cd autoclicker-ice
	````
	- if you using linux you need to change the permission first,this is how you do it
	````
	chmod +x main.py
	````
	and then run it with this command if you using linux
	````
	./main.py
	````
	or you just can run it with( windows or linux is ok)
	````
	py main.py
	python main.py
	python3 main.py
	````
	- and then you will enter the app
	
    ![enter image description here](http://imgur.com/ognAAYUl.png)
	
    - input number 1 to check the coordinates
	- and press CTRL + C to exit
	- that's all.
	
2.  Autoclicker with many position
	- First thing you need is where is the position that you will work on.
	- You can use Check coordinates in this app
	- then if you already know where is the position that you will work on
	- Put it into the setup in main.py
	- open main.py in your text editor
	- then see this line
	````python
	#------------------------------------
	#Setup
	#================================
	#Position 1
	x =  588 
	y =  331
	#if there is any Position ( Position 2 )
	x1 =  793
	y1 =  338
	#Just add some x2,y2, . . .
	#if there is more than 1 position
	#Time Delay
	delay =  0.1
	#Set Shortcut
	p = Key.f4 # Pause
	r = Key.f2 # Resume
	s = Key.esc # Exit / Stop
	#============================
	````
	 - put the position1 in x, y and position 2 is in x1, y1
	 - this is only if you will work on more than 1 position