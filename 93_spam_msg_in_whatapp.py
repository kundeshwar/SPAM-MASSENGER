import pyautogui as spam
import time 

limit = 2000
Msg = ("helo , helo bc mc")

time.sleep(10) # IT  gives complete your peocess in 4 minutes

for i in range(limit):
    spam.typewrite(Msg) # typewriter is a function which sending this msg 
    spam.press('Enter') # sending this above msg by using this key

    
    