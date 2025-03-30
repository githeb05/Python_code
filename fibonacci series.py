# Function definition 
def fibo(n): 
    if n == 1: 
        print(0) 
    else: 
        first = 0 
        second = 1 
        print(first) 
        print(second) 
        for i in range(2, n): 
            third = first + second 
            print(third) 
            first, second = second, third 

# Main  
n = int(input("Enter the limit: ")) 
fibo(n)
