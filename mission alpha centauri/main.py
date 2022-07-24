speedOfLight=1
planets={"Alpha Centauri":4.2,"Barnard's Star":5.96,"Luhman 16":6.59,"WISE 0855-0714":7.2,"Wolf 359":7.78}
numberOfSecondsPerYear=1
x=0
while x==0:
    planet=input("Choose your planet: ")
    if planet in planets:
        distance=speedOfLight*numberOfSecondsPerYear*planets.get(planet,2)
        print("The distance in km: "+str(distance))
        r=input("Do you want to continue? y/n: ")
        if r=="y":
            x=0
        else:
            x=1
    else:
        print("Your selected planet is not in list! Please choose a proper planet")
