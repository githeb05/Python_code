# Function definition
def findele(L, N):
    if N in L:
        print("Element is found in the list")
    else:
        print("Element entered is not found in the list")

# Main
L = eval(input("Enter a list: "))
N = input("Enter an element: ")
findele(L, N)
