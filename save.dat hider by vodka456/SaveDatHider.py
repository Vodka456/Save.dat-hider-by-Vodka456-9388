from pynput.keyboard import Key, Controller
keyboard = Controller ()
import os
import time
import random
import pynput
import socket
import shutil
import getpass

username = getpass.getuser()
print (username)
clear = lambda: os.system("cls")
print ("If The Directory Dosn't Exist This Prompt Will Close!")
time.sleep(1.5)
clear()


savedat=input("Please Enter Directory Of Save.dat")
os.remove(savedat)
print ("Removed ",savedat)
time.sleep(2)
clear()


print ("Adding Dummy save.dat Hold On...")
time.sleep(1)
clear()


file=open(savedat , 'w')
time.sleep(0.5)
file.close()

dummygen = input("Done!Deleted Save.dat And Replaced With New Save.dat,Thanks For Using Please Type a Number to Rate!")
print ("Thanks For Rating vodkaDeleter Thanks for",dummygen)
time.sleep(0.5)
exit()
