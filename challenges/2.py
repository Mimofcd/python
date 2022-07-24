text1="aaaa"
text2="abc"
def mid(text):
    if(len(text)%2==0):
        print("v")
        return("")
    else:
            middle=(len(text)-1)//2
            print(text[middle],middle)
            return text[middle]
        
mid(text1)
mid(text2)
