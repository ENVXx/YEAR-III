print("MCE 433 - Assignment #1\nElias Newall-Vuillemot - 9/10/2025\nQuestion I - Vector Adder")
input()
import math as m
import numpy as n
# Get user input for two 2D vectors
print("Vector A:")
iA = float(input("x component? "))
jA= float(input("y component? "))
print("Vector B:")
iB = float(input("x component? "))
jB= float(input("y component? "))

print("A + B =")
# Adding the vectors by component
iC = round(iA+iB,2)
jC = round(jA+jB,2)
# Finding the magnitued of the resultant vector
magC = round(m.sqrt(iC**2 + jC**2),2)
try: #I know atan2 exists, I just wanted to use the try/except features
    angC = round(m.degrees(m.atan(jC/iC)),2)
except ZeroDivisionError:
    if jC == 0 :
        print("The resultant is the null vector")
    else:
        angC = n.sign(jC)*90
        print(iC,"i ",jC,"j\n",magC," @",angC," deg")
else: # Print Results
    print(iC,"i ",jC,"j\n",magC," @",angC," deg")
input()