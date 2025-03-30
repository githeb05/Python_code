# Function definition 
def palin(string): 
    rev = string[::-1] 
    if string == rev: 
        print("It is a palindrome") 
    else: 
        print("It is not a palindrome")

# Main  
string = input("Enter the string: ") 
palin(string)
