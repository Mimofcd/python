import math


def math_puzzle1():
    print("two square numbers add up 36482")
    for i in range(0,1000):
        for j in range(0,i):
            if(pow(i,2)+pow(j,2)==36482):
                print(i)
                print(j)
                print(str(i)+"**2+"+str(j)+"**2=36482")
    exit()
def math_puzzle2():
    print("three square numbers add up 125")
    for i in range (0,1000):
        for j in range (0,i):
            for k in range (0,j):
                if((pow(i,2)+pow(j,2)+pow(k,2))==125):
                    print(i)
                    print(j)
                    print(k)
                    print(str(i)+"**2+"+str(j)+"+**2+"+str(k)+"**2=125")
    exit()
def math_puzzle3():
    print("what two integers numbers add up to 16 and multiply to 55")
    for i in range(0,1000):
        for j in range (0,i):
            if(i+j==16 and i*j==55):
                print(i)
                print(j)
                print(str(i)+"+"+str(j)+"=16\n"+str(i)+"*"+str(j)+"=55")
    exit()
def math_puzzle4():
    print("what are two prime number multiply to 3071?")
    for i in range(0,1000):
        for k in range(2,i//2):
            for j in range (0,i):
                for k2 in range (2,j//2):
                    if(i%k!=0 and j%k2!=0 and i*j==3071):
                        print(i)
                        print(j)
                        print("Prime numbers: "+str(i)+"*"+str(j)+"=3071")
    exit()  
math_puzzle1()
math_puzzle2()
math_puzzle3()
math_puzzle4()