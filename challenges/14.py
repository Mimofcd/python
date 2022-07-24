def palindrome(text):
    for i in range(0,int(len(text)/2)):
        if (text[i]!=text[(len(text)-1-i)]):
            print("False")
            return False
    print("True")
    return True

palindrome("abba")
palindrome("marmota")