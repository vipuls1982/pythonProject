from random import randint
from time import sleep
from os import system

system('cls')
count=int(input("how many addition you want to practice:"))


for i in range(1, count+1):

    system('cls')
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
        sleep(10)
        exit
    else :
        print(" ")

        
    system('cls')
    print("enter carry forward")
    print("                    " + str(a) )
    print("                  + " + str(b) )
    print("                ------------")
    print("                     " + str(c) )
    d=input()
    system('cls')

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
    system('cls')

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
    sleep(5)
    system('cls')
    i=i+1