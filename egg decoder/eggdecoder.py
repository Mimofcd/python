print("Please provide Egg Code Stamp: ")
x=str(input())
list_numbers=["0","1","2","3"]
list_country_short=[]
list_country_long=[]
with open('D:/Phyton/101computing/egg decoder/country-codes.txt') as f :
    list_text=f.read().splitlines()
# print (list_text[2][3:len(list_text[2])])
if(len(x)>=7):
    if x[0] in list_numbers:
        if x[0]=="0":
            r1="Organic"
        elif x[0]=="1":
            r1="Free range"
        elif x[0]=="2":
            r1="Barn"
        elif x[0]=="3":
            r1="Cage"
        country=x[1]+x[2]
        for item in range (0,len(list_text)):
            list_country_short.append(list_text[item][0:2])
            if(list_country_short[item]==country):
                r2=list_text[item][3:len(list_text)]
        if country in list_country_short:
                pass
        else:
            print("Country not in list")
            exit()
        print(" ",r1," Egg\n","Country of origin: ",r2,"\n","Farm Id: ",x[3:len(x)])
    else:
        print("Invalid code")
else:
    print("Invalid code")
    exit()