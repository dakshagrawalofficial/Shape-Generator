print("\n\n*********************************************************************************************************************************************************\n")
import turtle

def badValue() : 
    print("Invalid values entered!")
i = int()
t = turtle
shape = (str(input("Which shape do you want to draw? \n1. Square \n2. Rectangle \n3. Circle \n4. Equilateral Triangle \n5. Triangle \n6. Custom shape\nEnter the shape: "))).upper().replace(" ","").strip()
pencolor = (str(input("Enter the color of the pen: "))).capitalize().replace(" ","").strip()
t.pencolor(pencolor)
# fillcolor = (str(input("Enter the color of the shape from inside: "))).capitalize().replace(" ","").strip()
# t.fillcolor(fillcolor)

if (shape==("1" or "SQUARE" or "S")) :
    s = (float(input("Enter the length of sides of the square (in px): ")))
    while i <= 4:
        t.forward(s)
        t.left(90)
        i+=1
    
elif (shape==("2" or "RECTANGLE" or "R")) :
    l = (float(input("Enter the length of the rectangle (in px): ")))
    b = (float(input("Enter the breadth of the rectangle (in px): ")))
    t.penup()
    t.left(180)
    t.forward(l/2)
    t.right(90)
    t.pendown()
    while i <= 2:
        t.forward(b)
        t.right(90)
        t.forward(l)
        t.right(90)
        i += 1
    
elif (shape==("3" or "CIRCLE" or "C")) :
    r = (float(input("Enter the radius of the circle (in px): ")))
    t.circle(r)
    
elif (shape==("4" or "TRIANGLE" or "EQUILATERAL TRIANGLE" or "ET" or "EQUILATERAL" or "EQUILATERALTRIANGLE")) :
    s = (float(input("Enter the side of the triangle (in px): ")))
    t.penup()
    t.left(180)
    t.forward(s/2)
    t.right(120)
    t.pendown()
    while i <= 3 :
        t.forward(s)
        t.right(60)
        i += 1
    
elif (shape==("5" or "TRIANGLE" or "T")) :
    customSides = (str(input("Do you want different lengths for the sides of the triangle (Y/N) ? "))).upper()
    customAngles = (str(input("Do you want different interior angles for the triangle (Y/N) ? "))).upper()
    if customSides=="N" :
        s = (float(input("\nEnter each side of the triangle (in px): ")))
        t.penup()
        t.left(180)
        t.forward(s/2)
    elif customSides=="Y" :
        s1 = (float(input("Enter the length of the 1st side of the triangle (in px): ")))
        s2 = (float(input("Enter the length of the 2nd side of the triangle (in px): ")))
        s3 = (float(input("Enter the length of the 3rd side of the triangle (in px): ")))
        t.penup()
        t.left(180)
        t.forward(s1/2)
        t.pendown()
    else : 
        badValue()
    if customAngles=="N" :
        a = (float(input("\nWhat is the angle for each side of the triangle? ")))
    elif customAngles=="Y" :
        sumOfAngles = float()
        while sumOfAngles != 180:
            a1 = (float(input("Enter the 1st angle of the triangle: ")))
            a2 = (float(input("Enter the 2nd angle of the triangle: ")))
            a3 = (float(input("Enter the 3rd angle of the triangle: ")))
            sumOfAngles = a1+a2+a3
            if sumOfAngles != 180 :
                print("\nThe sum of the angles are not equal to 180°, so please re-enter the values.")
    else : 
        badValue()
    if customSides=="Y" :
        if customAngles=="Y" :
            t.right(a1)
            t.forward(s1)
            t.right(a2)
            t.forward(s1)
            t.right(a3)
            t.forward(s3)
        elif customAngles=="N" :
            t.right(a)
            t.forward(s1)
            t.right(a)
            t.forward(s1)
            t.right(a)
            t.forward(s3)
    elif customSides=="N" : 
        if customAngles=="Y" :
            t.right(a1)
            t.forward(s)
            t.right(a2)
            t.forward(s)
            t.right(a3)
            t.forward(s)
        elif customAngles=="N" :
            t.right(a)
            t.forward(s)
            t.right(a)
            t.forward(s)
            t.right(a)
            t.forward(s)
    
elif (shape==("6" or "CUSTOM" or "CUSTOM SHAPE" or "CUSTOMSHAPE" or "CS" or "SHAPE")) :
    l = float(input("Enter the length of the lines drawn: "))
    a = float(input("Enter the angle of every turn the turtle takes: "))
    while (l != ("" or 0)):
        t.forward(l)
        t.right(a)
        l = float(input("Enter the length of the lines drawn (Enter key or 0 to exit): "))
    
else :
    badValue()
    

t.done()
print("\n\n")