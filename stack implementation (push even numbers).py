EVEN = []  

def PUSH(Num):  
    for n in Num:  
        if n % 2 == 0:  
            EVEN.append(n)  

    if EVEN != []:  
        print("Stack with even values", EVEN)  
    else:  
        print("Stack is empty")  

# Main  
Num = eval(input("Enter some numbers to separate: "))  
PUSH(Num)
