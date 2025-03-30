import pickle 

# Writing into the file 
f = open("stu.dat", "wb") 
s = {} 

ch = "y" 
while ch == "y": 
    roll = int(input("Enter the roll number: ")) 
    name = input("Enter the name: ") 
    s["Rollno"] = roll 
    s["Name"] = name 
    pickle.dump(s, f) 
    ch = input("Do you want to continue? (y/n): ") 

f.close() 

# Reading from file 
f = open("stu.dat", "rb") 
found = False 

try: 
    s = int(input("Enter the roll number to be searched: ")) 

    while True: 
        d = pickle.load(f) 
        if d["Rollno"] == s: 
            print(d["Name"]) 
            found = True 
except EOFError: 
    if not found: 
        print("No such records") 
    else: 
        print("Search successful") 

f.close()
