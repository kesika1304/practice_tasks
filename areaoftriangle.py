Base = float(input("Enter breath of triangle:   "))
Height = float(input("Enter height of triangle:     "))

Area = 0.5*Base*Height

print('Area of triangle = %f' %Area)


#Using funtion

def Area(a,b):
    return a*b*0.5
Base = float(input("Enter breath of triangle:   "))
Height = float(input("Enter height of triangle:     "))
print("Area of triangle %f" %Area(Base,Height))

