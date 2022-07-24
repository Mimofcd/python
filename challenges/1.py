text1="HelLO My name is MIHAI"
def capital_indexes(text1):
        char_list=[]
        for index,char in enumerate(text1):
            if char.isupper():
                char_list.append(index)
        print (char_list)
        return (char_list)
capital_indexes(text1)