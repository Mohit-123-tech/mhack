
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
        print(f"som is --< {som}")

    elif code=='sup':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1-n2
        print(f"som is --< {som}")

    elif code=='multi':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1*n2
        print(f"som is --< {som}")

    elif code=='div':
        n1 = int(input("Enter a value --< "))
        n2 = int(input("Enter a value --< "))
        som = n1/n2
        print(f"som is --< {som}")

    elif code=='sqrt':
        n1 = int(input("Enter a value --< "))
        print(f"sqrt is --< {math.sqrt(n1)}")

    elif code=='--help':
        open(help.txt)
    
    else :
        print("commad not found !!!")

        

