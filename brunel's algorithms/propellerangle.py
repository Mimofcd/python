import math
def calculateAngle(noblades):
    angle=360/noblades
    print(angle)
    return angle
def ArchWidth(len,noarches):
    width=len/noarches
    print(width)
    return width
def calculatePercentSlope(x,h):
    slope=(h/x)*100
    print(slope)
    return slope
def calculateArcLength(l,h):
    radius=h/2+pow(l,2)/(8*h)
    print(radius)
    theta=2/math.sin(math.radians(l/(2*radius)))
    print(theta)
    arc_len=2*math.pi*radius*(theta/360)
    print(arc_len)
    return arc_len

# calculateAngle(4)
# calculateAngle(6)
# ArchWidth(270,8)
# ArchWidth(230,9)
# calculatePercentSlope(800,32)
# calculatePercentSlope(500,60)
calculateArcLength(214,26)