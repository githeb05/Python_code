stack = []  

def PUSH():  
    item = eval(input("Enter the element to push: "))  
    stack.append(item)  
    print("Stack after push -->", stack)  

def POP():  
    if stack == []:  
        print("Stack is empty")  
    else:  
        stack.pop()  
        print("Stack after pop -->", stack)  

# Main  
print("1. PUSH\n2. POP")  
ch = 'y'  

while ch in 'Yy':  
    choice = int(input("Enter your choice: "))  
    if choice == 1:  
        PUSH()  
    elif choice == 2:  
        POP()  
    else:  
        print("Invalid choice!!")  
    ch = input("\nDo you want to continue (Y/N)? ")
