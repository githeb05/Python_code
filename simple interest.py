# Function to calculate simple interest with default values  
def interest(principal, time=2, rate=0.10):  
    return principal * rate * time  

# Main  
prin = float(input("Enter principal amount: "))  
si1 = interest(prin)  
print("Simple interest with default ROI and time values is:", "Rs.", si1)  

roi = float(input("Enter rate of interest (ROI): "))  
time = int(input("Enter time in years: "))  
si2 = interest(prin, time, roi / 100)  
print("Simple interest with your provided ROI and time values is:", "Rs", si2)
