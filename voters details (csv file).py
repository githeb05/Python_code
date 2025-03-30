import csv 

# Writing into the CSV file 
f = open("Voters.csv", "w", newline="") 
w = csv.writer(f) 

ch = 'y' 
while ch == 'y': 
    id = int(input("Enter voter ID: ")) 
    name = input("Enter the name: ") 
    age = int(input("Enter the age: ")) 
    w.writerow([id, name, age]) 
    ch = input("Do you want to continue? (y/n): ") 

f.close() 

# Reading from CSV file 
f = open("Voters.csv", "r") 
r = csv.reader(f) 

print("Voter details whose age is more than 65:") 
for a in r: 
    if int(a[2]) > 65: 
        print(a) 

f.close()
