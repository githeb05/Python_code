# Writing to file 
f = open('data.txt', 'w') 
L = eval(input("Enter the data: ")) 
f.writelines(L)  # Writing into the file 
f.close() 

# Reading from file 
f = open("data.txt", "r") 
r = f.read(1) 

cv = cc = cu = cl = 0 

while r: 
    if r.isalpha():  
        if r in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']: 
            cv += 1 
        else: 
            cc += 1 

        if r.isupper(): 
            cu += 1 
        else: 
            cl += 1 

    r = f.read(1) 

f.close() 

print("Number of vowels:", cv) 
print("Number of consonants:", cc) 
print("Number of uppercase letters:", cu) 
print("Number of lowercase letters:", cl)
