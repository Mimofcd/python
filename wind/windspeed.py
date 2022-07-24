forces = {0: ["Calm","Sea like a mirror","Smoke rises vertically"],
          1: ["Light air","Ripples with appearance of scales are formed, without foam crests","Direction shown by smoke drift but not by wind vanes."],
          2: ["Light breeze","Small wavelets still short but more pronounced; crests have a glassy appearance but do not break","Wind felt on face; leaves rustle; wind vane moved by wind."],
          3: ["Gentle breeze","Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses","Leaves and small twigs in constant motion; light flags extended."],
          4: ["Moderate breeze","Small waves becoming longer; fairly frequent white horses","Raises dust and loose paper; small branches moved."],
          5: ["Fresh breeze","Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray","Small trees in leaf begin to sway; crested wavelets form on inland waters."],
          6: ["Strong breeze","Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray","Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
          7: ["High wind, moderate gale, near gale","Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of the wind; spindrift begins to be seen","Whole trees in motion; inconvenience felt when walking against the wind."],
          8: ["Gale, fresh gale","Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in well-marked streaks along the direction of the wind","Twigs break off trees; generally impedes progress."],
          9: ["Strong/severe gale","High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects visibility","Slight structural damage (chimney pots and slates removed)."],
          10: ["Storm, whole gale","Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white streaks along the direction of the wind; on the whole the surface of the sea takes on a white appearance; rolling of the sea becomes heavy; visibility affected","Seldom experienced inland; trees uprooted; considerable structural damage."],
          11: ["Violent storm","Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests are blown into foam; visibility affected","Very rarely experienced; accompanied by widespread damage."],
          12: ["Hurricane force","The air is filled with foam and spray; sea is completely white with driving spray; visibility very seriously affected","Devastation"]
          }
# print(forces.get(3)[1])
def input_speed():
    unit=str(input("Enter desired unit (km/h,mph,knots): "))
    if(unit=="km/h" or unit=="mph" or unit=="knots"):
        if(unit=="km/h"):
            speed=int(input("Enter speed in km/h: "))
            speed_knot=speed*1.852
            return speed_knot
        if(unit=="mph"):
            speed=int(input("Enter speed in mph: "))
            speed_knot=speed*1.15
            return speed_knot
        if(unit=="knots"):
            speed_knot=int(input("Enter speed in knots: "))
            return speed_knot
    else:
        print("Wrong unit")
        exit()
# def conv_knots(speed):
#     speed_kn=speed*1.852
#     print (speed_kn)
#     return speed_kn
def scale(speed):
    if speed<1:
        return 0
    elif 1<=speed<=3:
        return 1
    elif 4<=speed<=6:
        return 2
    elif 7<=speed<=10:
        return 3
    elif 11<=speed<=16:
        return 4
    elif 17<=speed<=21:
        return 5
    elif 22<=speed<=27:
        return 6
    elif 28<=speed<=33:
        return 7
    elif 34<=speed<=40:
        return 8
    elif 41<=speed<=47:
        return 9
    elif 48<=speed<=55:
        return 10
    elif 56<=speed<=63:
        return 11
    elif speed>=64:
        return 12
knots=input_speed()
print(knots)
scale=scale(knots)
print(forces.get(scale)[0]+"\n"+forces.get(scale)[1]+"\n"+forces.get(scale)[2])