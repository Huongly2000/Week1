# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 13:44:58 2025

@author: ADMIN
"""

# Exercise 1: Working with Strings and Booleans
#a. Assign each line separately to a variable as a string.
line1 = "Python was created by Guido van Rossum, a Dutch programmer."
line2 = "First version of Python 0.9.0 was developed in Centrum Wiskunde & Informatica (CWI) in the Netherlands in 1991."
line3 = "Python 3.0 was released on 3 December 2008."

#b. Check if the variables are of type string.
print(type(line1))
print(type(line2))
print(type(line3))

#c. If all three variables return <class 'str'>, then create three new boolean variables (e.g., A = True) to represent this.
A = True
B = True
C = True

#d. Write a boolean expression (using ==, and, or both) that confirms all three variables are string data types.
print(A and B and C)
print(type(line1) == str and type(line2) == str and type(line3) == str)

#e. Print all three lines together in the console (on separate lines).
print(line1)
print(line2)
print(line3)

import math

# Exercise 2:Calculating the Future Value of an Ordinary Annuity
#a.Calculating the Future Value of an Ordinary Annuity
C1 = 2000
i1 = 0.05
n1 = 7

FV = C1 * (math.pow(1+i1,n1)-1)/i1

print("Worth of future value at the end of 7 years (rounded to 2 decimals) is £", round(FV, 2))

#b.Calculating the Present Value of an Annuity Due
C2 = 1000
i2 = 0.05
n2 = 5

PV = C2 * ((1-math.pow(1+i2,-n2)) / i2) * (1+i2)

print("Present Value of the Annuity Due (rounded to 2 decimals): £", round(PV, 2))

# Exercise 3: Cryptocurrency Conversion
BTC_Amount = 0.5
BTC_Price = 40000
ETH_Price = 2000

BTC_Value = BTC_Amount*BTC_Price
ETH_Amount = BTC_Value/ETH_Price

print("You own", BTC_Amount, "BTC.")
print("Value in £:", BTC_Value)
print("If converted to Ethereum, you would have:", round(ETH_Amount, 2), "ETH")

# Exercise 4: Debug the following piece of code
divide_by = 2
subtract_by = 3

var = 1
var1 = int(var) - subtract_by
print("Subtracting your value of", var, "by", subtract_by, "will give", var1)
# Alternative way to print
# print("Subtracting your value of "+ str(var) +" by "+ str(subtract_by) +" will give "+ str(var1))

var2 = var1 / divide_by
print("Dividing", var1, "by", divide_by, "will give", var2)


var3 = 0.5
print("The ceiling of", var3, "is", math.ceil(float(var3)))

var4 = 2
var5 = 3

print("Multiplying", var4, "by", var5, "will give", var4*int(var5))
print("Multiplying", var4, "by", var5, "will give", int(var4)*int(var5))
print("Multiplying", float(var4), "by", var5, "will give", float(var4)*int(var5))






