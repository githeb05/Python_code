import pickle 

# Writing into the file 
f = open("student.dat", "wb") 
s = {} 

ch = "y" 
while ch == "y": 
    roll = int(input("Enter the roll number: ")) 
    name = input("Enter the name: ")) 
    mark = float(input("Enter the mark: ")) 
    s["Rollno"] = roll 
    s["Name"] = name 
    s["Mark"] = mark 
    pickle.dump(s, f) 
    ch = input("Do you want to continue? (y/n): ")  

f.close() 

# Reading and updating file 
f = open("student.dat", "rb+") 
found = False 

try: 
    s = int(input("Enter the roll number to be updated: "))  

    while True: 
        p = f.tell() 
        d = pickle.load(f) 

        if d["Rollno"] == s: 
            f.seek(p) 
            d["Mark"] = int(input("Enter the new mark: ")) 
            pickle.dump(d, f) 
            found = True 
            break 
except EOFError: 
    f.close()  

if not found: 
    print("No such records") 
else: 
    print("Mark updated") 
