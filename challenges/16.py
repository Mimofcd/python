def consecutive_zeros(text):
    count=0
    result=0
    for x in text:
        if x=="0":
            count=count+1
            result=max(result,count)
        else:
            count=0
    print(result)
    return(result)
    
    
consecutive_zeros("100100010")