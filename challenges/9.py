from operator import is_


def is_anagram(t1,t2):
    if(sorted(t1)==sorted(t2)):
        print("True")
        return True
    else:
        print("False")
        return False
is_anagram("listen","silent")
is_anagram("Bob","Andy")
