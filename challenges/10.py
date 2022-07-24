def flatten(list1):
    list2=[]
    for x in list1:
        for item in x:
            list2.append(item)
    print (list2)
    return list2

flatten([[1,2],[3,4],[5,8,9]])

