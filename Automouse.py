import pyautogui
import time
import random

for z in range(1,500):
    x=random.randint(0,500)
    y =random.randint(0,500)
    pyautogui.moveTo(x,y)

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p",localtime) #Indicate the Time

    print('Moved at '+ str(result)+ '('+str(x)+','+str(y)+')') #Print the moved time & x,y Cordinates
    time.sleep(10) #You can change the next mouse point moving time
