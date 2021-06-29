
import datetime
import os
import math

uname = input("name --< ")

for i in range(1,100000000):
    code = input(f"[{uname}]--({i})\n----λ ")
    if code=='table':
        num = int(input("Enter a number --< "))
        for i in range(1,11):
            print(f"{ num } x { i } = {num * i} ")

    elif code=='exit':
        exit()

    elif code=='add':
        num1 = int(input("Enter a value --< "))
        num2 = int(input("Enter a value --< "))
        som = num1+num2
        print(f"{num1} + {num2} = {som}")

    elif code=='sup':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1-n2
        print(f"{num1} - {num2} = {som}")

    elif code=='multi':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1*n2
        print(f"{num1} x {num2} = {som}")

    elif code=='div':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1/n2
        print(f"{num1} % {num2} = {som}")

    elif code=='sqrt':
        n1 = int(input("Enter a value --< "))
        print(f"sqrt is --< {math.sqrt(n1)}")
        
    elif code=='date':
        dt = datetime.datetime.now()
        print(dt)
    
    elif code=='clear':
        os.system("clear")
        
    elif code=='str-size':
        name = input('text --> ')
        print(len(name))
        
    elif code=='c-list':
        print("==========command list==========")
        print('date')
        print('add')
        print('clear')
        print('sup')
        print('multi')
        print('div')
        print('c-list')
        print('sqrt')
        print('table')
        print('str-size')
        print('name')
        print('cmatrix')
        
    elif code=='cmatrix':
        os.system('apt-get install cmatrix -y')
        os.system('clear')
        os.system('cmatrix')
        
    elif code=='name':
        uname = input('change your name --£ ')
              
    else :
        print("commad is not added !!!")

        

