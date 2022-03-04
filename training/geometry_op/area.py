from perimeter import * 
import math

obj=g_data('','',[])

def area(obj):
    shape=obj.geometricShape.lower()
    if shape =='circle': 
        area=setarea_of_circle(obj.radius)
        return area
    elif(shape =='triangle'):
        area=setareac_of_triangle(obj.sides)
        return area
    elif(shape =='rectangle'):
        area= setareac_of_rectangle(obj.sides)
        return area
    else:
        return -1


def setarea_of_circle(r):
    if(r):
        area_circle=3.14*r*r
        return area_circle
    else: return "invalid input"    


def setareac_of_triangle(s):
    if len(s)==3:
        pm=0;
        for x in s:
            pm+=int(x)
        semi_pm= pm/2 
        area_tr=math.sqrt(semi_pm*(semi_pm-int(s[0]))*(semi_pm-int(s[1]))*(semi_pm-int(s[2])))
        return area_tr
    else: 
        return "invalid input"
    

def setareac_of_rectangle(s):
    if len(s)==4:
        s.sort()
        area_rectangle=int(s[0])*int(s[2])
        return area_rectangle 
    else: return "invalid input"   

if __name__ == "__main__":
    data = {"shape": "circle", "radius": 7}
    data_obj = g_data(data.get('shape'), data.get('radius'))
    print(dir(data_obj))
    obj_area = area(data_obj)
    if obj_area == -1:
        print("Error: Unrecognised shape.")
    print("area of object: {}".format(obj_area))




