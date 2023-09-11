from random import *
r=randint(1,100)
def num():
    while True:
        num=input("enter number")
        if num=="exit":
            print("exit the program succesfully")
            break
        if r>int(num) : print("up")
        if r<int(num) : print("dn")
        if r==int(num):
            print("your number is :" ,r," correct")
            break
num()