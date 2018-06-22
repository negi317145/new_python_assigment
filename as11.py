#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
from threading import Thread
import time

def display():
  print("Wait for 2 seconds\n")
  time.sleep(2)
  print("Hey Himanshu Negi")
  
t=Thread(target= display)
t.setName("hello python")
t.start()


print("\n*******************************\n")




#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between 

def display(num):
  for x in range(num):
    print(x)
    time.sleep(1)
num=10
t=Thread(target=display,args=(num,))
t.start()

 
#Q3. a delay of multiple of 2 sec between each display.

def display():
  l=[1,2,3,4,5]
  for x in l:
    print(x)
    time.sleep(2)


t=Thread(target=display)
t.start()

print("\n*******************************\n")



#Call factorial function using thread.
import math
def factorial(num):
  print("wait 2 seconds for result")
  time.sleep(2)
  print("factorial is:",math.factorial(num))


num=int(input("enter any no. to find factorial\n"))
t=Thread(target=factorial(num))
t.start()


