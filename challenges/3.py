dict1={
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(dict):
    x=0
    for xr in dict.values():
        if xr=="online":
            x=x+1
    print(x)
    return x
online_count(dict1)