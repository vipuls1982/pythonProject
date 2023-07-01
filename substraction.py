from random import randint
from time import sleep
from os import system

system('cls')
count=int(input("how many substraction you want to practice:"))


for i in range(1, count+1):

    system('cls')
    a=randint(10,99)
    b=randint(10,a)
    sub=a-b
    once=sub % 10
    if((a % 10) - (b % 10) < 0): 
        cf=-1
        cf1=""
    else:
        cf=0
        cf1=" "


    tens=sub // 10


    print("                   " + str(a) )
    print("                 - " + str(b) )
    print("               ------------")
    #print("enter once digit")
    #c=input()
    #print("                   " + str(a) + "\n""                 + " + str(b)+ "\n               ------------\n" +"                    {0}".format(input("enter once digit:   ")))
    c=input("enter once digit:   ")
    if int(c) != int(once):
        print("Sorry, once digit is not correct rignt ans is " + str(once))
        c=input() 
        sleep(10)
        exit
    else :
        print(" ")

        
    system('cls')
    print("enter carry forward")
    print("                    " + str(a) )
    print("                  - " + str(b) )
    print("                ------------")
    print("                     " + str(c) )
    d=input()
    system('cls')

    if int(d) != int(cf):
        print("Sorry, carryforward is not correct rignt ans is " + str(cf)+ "\n please enter carryforward again") 
        d=input()
        exit
    else :
        print(" ")


    print("                   "+cf1 + str(d))
    print("                    " + str(a) )
    print("                  - " + str(b) )
    print("                ------------")
    print("input tens digit     " + str(c) )
    e=input()
    system('cls')

    if int(e) != int(tens) :
        print("Sorry, tens is not correct rignt ans is " + str(tens)+ "\n please enter carryforward again") 
        e=input()
        exit
    else :
        print(" ")

    print("                   "+cf1 + str(d))
    print("                    " + str(a) )
    print("                  - " + str(b) )
    print("                ------------")
    print("                    "+ str(e) + str(c) )


    #print(str(ei)+ "!="+ str(tot))
    if (int(e)*10+int(c)) != int(sub) :
        print("Sorry, total is not correct rignt ans is " + str(sub)) 
        exit
    else :
        print("\n\n\n Hurray!!!!!!!!!! its correct")
    sleep(8)
    system('cls')
    i=i+1