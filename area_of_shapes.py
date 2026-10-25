def return_area(shape ,*args):
    result=0
    if shape == "square":
        result=args[0]**2
    elif shape == "triangle":
        result= 0.5*args[0]*args[1]
    elif shape == "circle":
        result=3.14*(args[0]**2)
    elif shape =="cone":
        result= 3.14*(args[0]**2)*args[1]
    return result
    
print(return_area("square", 2))
print(return_area("triangle", 2,4))
print(return_area("circle", 2))
print(return_area("cone", 2,4))