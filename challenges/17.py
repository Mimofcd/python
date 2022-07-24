from asyncio.windows_events import NULL


def all_equal(list):
    if len(list)==0:
        return True
    else:
        el1=list[0]
        count=0
        for item in range(len(list)):
            if el1 == list[item]:
                count+=1
        if count==len(list):
            print("True")
            return True
        else:
            print("False")
            return False
            

all_equal([1,1,1])
all_equal([1])
all_equal([])
all_equal(["a",1,3])
all_equal(["a","a","A"])