import math 

def cls(): 
    print("#" * 50) 

def circle(r):  # Circle area - definition 
    return math.pi * r * r 

def rectangle(l, b):  # Rectangle area - definition 
    return l * b 

def square(a):  # Square area - definition 
    return a * a 

# Main  
while True: 
    cls() 
    print("\t\tAREA CALCULATION") 
    print("\t\t1. Circle") 
    print("\t\t2. Rectangle") 
    print("\t\t3. Square") 
    print("\t\t4. Exit") 

    ch = int(input("Enter your choice: ")) 
    if ch == 1: 
        r = int(input("Enter the radius: ")) 
        print("Area of circle is:", circle(r))         
    elif ch == 2: 
        l = int(input("Enter the length: ")) 
        b = int(input("Enter the breadth: ")) 
        print("Area of rectangle is:", rectangle(l, b)) 
    elif ch == 3: 
        a = int(input("Enter the side: ")) 
        print("Area of square is:", square(a)) 
    elif ch == 4: 
        break 
    else: 
        print("Invalid choice")
