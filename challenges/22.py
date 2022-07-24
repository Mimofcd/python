def list_xor(n,list1,list2):
        if n in list1 and n not in list2:
            return True
        if n in list2 and n not in list1:
            return True
        if n in list1 and n in list2:
            return False
        if n not in list1 and n not in list2:
            return False