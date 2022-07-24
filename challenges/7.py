def add_dots(text):
    res=".".join(str(x) for x in text)
    print (res)
    return res
def remove_dots(text):
    res=text.replace(".","")
    print(res)
    return res
add_dots("mihai")
remove_dots(add_dots("mihai"))