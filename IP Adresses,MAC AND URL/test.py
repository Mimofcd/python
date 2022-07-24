from ipaddress import ip_address
from random import randint
import random
ip_address_gen_v4=str(randint(0,255))+"."+str(randint(0,255))+"."+str(randint(0,255))+"."+str(randint(0,255))
print(ip_address_gen_v4)
hex_string='ABCDEF0123456789'
ip_address_gen_v6=''.join([random.choice(hex_string) for x in range(4)])+"."+''.join([random.choice(hex_string) for x in range(4)])+"."+''.join([random.choice(hex_string) for x in range(4)])+"."+''.join([random.choice(hex_string) for x in range(4)])
print(ip_address_gen_v6)
mac_address_gen=''.join([random.choice(hex_string) for x in range(2)])+":"+''.join([random.choice(hex_string) for x in range(2)])+":"+''.join([random.choice(hex_string) for x in range(2)])+":"+''.join([random.choice(hex_string) for x in range(2)])+":"+''.join([random.choice(hex_string) for x in range(2)])+":"+''.join([random.choice(hex_string) for x in range(2)])
print(mac_address_gen)
url=str(input())
protocol1=url[0:4]
protocol2=url[0:5]
if(protocol2=="https"):
    print("Protocol: ",protocol2,"\n")
    domain=url[8:len(url)].partition('/')
    print("Domain: ",domain[0],"\n")
    folder_str=domain[2].partition('/')
    print("Folder structure: ",folder_str[0],"\n")
    file_name=folder_str[2]
    print("File name: ",file_name)
elif(protocol1=="http"):
    print("Protocol: ",protocol1,"\n")
    domain=url[7:len(url)].partition('/')
    print("Domain: ",domain[0],"\n")
    folder_str=domain[2].partition('/')
    print("Folder structure: ",folder_str[0],"\n")
    file_name=folder_str[2]
    print("File name: ",file_name)
else:
    print("Wrong protocol")
    exit()
# https://www.101computing.net/ip-addresses-ipv4-ipv6-mac-addresses-urls/index.html