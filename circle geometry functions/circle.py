import math
from webbrowser import get
def get_circumference(radius):
    circ=2*math.pi*radius
    return circ
def get_area(radius):
    area=math.pi*pow(radius,2)
    return area
def get_lengtharc(radius,angle):
    len_arc=2*math.pi*radius*(angle/360)
    return len_arc
def get_persector(radius,angle):
    per_sector=(2*math.pi*radius*(angle/360))+2*radius
    return per_sector
def get_areasector(radius,angle):
    area_sector=math.pi*pow(radius,2)*(angle/360)
    return area_sector
def get_chordlength(radius,angle):
    chord_length=2*radius*math.sin(math.radians(angle)/2)
    return chord_length
def get_persegm(radius,angle):
    per_segment=2*math.pi*(angle/360)+2*radius*math.sin(math.radians(angle)/360)
    return per_segment
def get_areasegm(radius,angle):
    area_segment=pow(radius,2)*(math.pi*(angle/360)-1/2*math.sin(math.radians(angle)))
    return area_segment
r=int(input("Enter the radius of a circle (r): "))
a=int(input("Enter the angle of an arc (a): "))
circumference=get_circumference(r)
print("The circumference of the circle is: "+str(circumference))
area=get_area(r)
print("The area of the circle is: "+str(area))
len_arc=get_lengtharc(r,a)
print("The legth of this arc is: "+str(len_arc))
per_sector=get_persector(r,a)
print("The perimenter of this sector is :"+str(per_sector))
area_sector=get_areasector(r,a)
print("The area of this sector is "+str(area_sector))
chord_length=get_chordlength(r,a)
print("The length of the chord is: "+str(chord_length))
per_segment=get_persegm(r,a)
print("The perimeter of the segment is: "+str(per_segment))
area_segment=get_areasegm(r,a)
print("The area of the segment is :"+str(area_segment))
