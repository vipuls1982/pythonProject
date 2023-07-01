from random import randint
import time
import os

os.system('cls')
count=int(input("how many substraction you want to practice:"))


for i in range(1, count+1):

    os.system('cls')
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
        time.sleep(10)
        exit
    else :
        print(" ")

        
    os.system('cls')
    print("enter carry forward")
    print("                    " + str(a) )
    print("                  - " + str(b) )
    print("                ------------")
    print("                     " + str(c) )
    d=input()
    os.system('cls')

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
    os.system('cls')

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
    time.sleep(8)
    os.system('cls')
    i=i+1