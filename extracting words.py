# Writing to file 
f = open("word.txt", "w") 

ch = 1 
while ch: 
    Line = input("Enter a line: ") 
    f.write(Line + "\n") 
    ch = int(input("Do you want to continue? (1/0): ")) 

f.close() 

# Reading from file 
f = open("word.txt", "r") 
for i in f: 
    for s in i.split():  # Extracting word by word 
        print(s, end="#") 
    print() 

f.close()
