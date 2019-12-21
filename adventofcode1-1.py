import math

totalFuel = 0 

aocinput=open("aocinput1.txt", "r") #opening input file
f1 = aocinput.readlines() #reading input txt file
for mass in f1:
    fuel = math.floor(int(mass)/3)-2
    totalFuel += fuel

print(totalFuel)
    
 
