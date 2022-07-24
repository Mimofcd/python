def double_letters(text):
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            print ("True")
            return True
    print("False")
    return False
double_letters("nonono")
double_letters("hello")