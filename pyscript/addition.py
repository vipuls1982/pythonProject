import main
from random import randint
import time
import os

os.system('cls')
count=int(input("how many addition you want to practice:"))


for i in range(1, count+1):

    os.system('cls')
    a=randint(10,99)
    b=randint(10,99)
    tot=a+b
    once=tot % 10
    cf= ((a % 10) + (b % 10)) // 10
    cf1=cf // 10
    tens=tot // 10


    print("                   " + str(a) )
    print("                 + " + str(b) )
    print("               ------------")
    #print("enter once digit")
    #c=input()
    #print("                   " + str(a) + "\n""                 + " + str(b)+ "\n               ------------\n" +"                    {0}".format(input("enter once digit:   ")))
    c=input("enter once digit:   ")
    if str(c) != str(once):
        print("Sorry, once digit is not correct rignt ans is " + str(once))
        c=input() 
        time.sleep(10)
        exit
    else :
        print(" ")

        
    os.system('cls')
    print("enter carry forward")
    print("                    " + str(a) )
    print("                  + " + str(b) )
    print("                ------------")
    print("                     " + str(c) )
    d=input()
    os.system('cls')

    if str(d) != str(cf):
        print("Sorry, carryforward is not correct rignt ans is " + str(cf)+ "\n please enter carryforward again") 
        d=input()
        exit
    else :
        print(" ")


    print("                    " + str(d))
    print("                    " + str(a) )
    print("                  + " + str(b) )
    print("                ------------")
    print("input tens digit     " + str(c) )
    e=input()
    os.system('cls')

    if str(e) != str(tens) :
        print("Sorry, tens is not correct rignt ans is " + str(tens)+ "\n please enter carryforward again") 
        e=input()
        exit
    else :
        print(" ")

    print("                    " + str(d))
    print("                    " + str(a) )
    print("                  + " + str(b) )
    print("                ------------")
    print("                    "+ str(e) + str(c) )


    #print(str(ei)+ "!="+ str(tot))
    if (str(e)+str(c)) != str(tot) :
        print("Sorry, total is not correct rignt ans is " + str(tot)) 
        exit
    else :
        print("\n\n\n Hurray!!!!!!!!!! its correct")
    time.sleep(5)
    os.system('cls')
    i=i+1