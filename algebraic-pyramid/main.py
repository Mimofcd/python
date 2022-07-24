from random import randint
from numpy import append
import py

def print_pyramid(pyramid):
    lines=[]
    for layer in pyramid:
        line=""
        for brick in layer:
            line+=str(brick)
            line+=" "
        lines.append(line)
    pyramid_len=max([len(layer) for layer in lines])
    txt=""
    for line in lines:
        dif=(pyramid_len-len(line))/2
        txt+=" "*int(dif+0.5)
        txt+=line
        txt+=" "*int(dif-0.5)
        txt+="\n"
    print(txt)
def calcul_pyramid(base):
    pyramid=[base]
    for i in range(len(base)-1):
        actual_layer=[]
        last_layer=pyramid[i]
        for j in range(len(last_layer)-1):
            actual_layer.append(last_layer[j]+last_layer[j+1])
        pyramid.append(actual_layer)
    return pyramid
def random_base(length):
        base=[]
        for i in range(length):
            base.append(randint(0,100))
        return base
# base=[1,2,3,4,5,6]
n=int(input("Please provide length of base: "))
base=random_base(n)
pyramid=calcul_pyramid(base)
print_pyramid(pyramid)
