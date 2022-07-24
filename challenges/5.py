import numbers
def only_ints(a,b):
    if type (a) in (int,float) and type(b) in (int,float):
        print("true")
        return True
    else:
        print("false")
        return False

only_ints("a",2)
only_ints(1,2)
only_ints(1,True)