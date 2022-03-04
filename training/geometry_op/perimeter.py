class g_data:
    def __init__(self,geometricShape, radius, sides=None):
        self.geometricShape : str = geometricShape
        self.radius : int = radius
        self.sides: list = sides


def perimeter(obj):
    print("inside perimeter - Object: ", type(obj))
    shape=obj.geometricShape.lower()
    print("shape - {}".format(shape))
    if shape =="circle":
        pm= circumference_circle(obj["radius"])
        return pm
    elif shape == "triangle" or shape == "rectangle":
        print(obj["sides"])
        pm=pm_triangleNrectangle(obj["sides"],shape)
        return pm
    else :
        return []    


def circumference_circle(r):
    if(r):
        pm=2*3.14*r
        return pm
    else: return "inavlid input"    


def pm_triangleNrectangle(s,shape):
    if((len(s)==3) and (shape=="triangle")) or ((len(s)==4) and (shape=="rectangle")):
        pm=0
        for i in s:
            pm+=int(i)
        return pm
    else: return "invalid input"      

if __name__ == "__main__":
    obj=g_data("","",[])
    print("inside main - Object: ", type(obj))
    perimeter(obj)

