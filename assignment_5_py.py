# -*- coding: utf-8 -*-
"""assignment 5.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hT3tfWSbpRLlkDwGzGEs8XnKjWa7ziPd

1.  write a program to find the area of a circle using math functions.
"""

import math
r= float(input("Enter the radius of the circle: "))
area= math.pi*(math.pow(r,2))
result= round(area,3)
print("The area of the circle with radius",r,"is:",result)

"""2.write a program to find the area of a regular polygon using math functions."""

s= float(input("Enter length of any side: "))
n= int(input("Enter number of sides in regular polygon: "))
numerator= math.pow(s,2)*n
denominator= 4*(math.tan(math.pi/n))
area= numerator/denominator
print("area of the regular polygon is:",area)

"""3. Program to find the area of a segment of a circle using math functions."""

import math
r= float(input("Enter radius of the circle: "))
c= int(input("Enter value of centra angle in degrees: "))
part_one= (math.pow(r,2))/2
part_two= ((((math.pi)/180)*c)-math.sin(c))
area= part_one*part_two
print("Area of segment of circle of radius",r, "and central angle",c,"is:",area)

"""4.write a program to shuffle a list."""

from random import shuffle
list=[70,5,6,1,56,46,"HI","DEAR"]
print("List before shuffling:",list)
shuffle(list)
print("List after shuffling:",list)

5. Program to generate random numbers between 1 and 10,000 and difference between each random number is 50.

import random
print("random number between 1 and 10000 which has step of 50:",random.randrange(1,10000,50))

"""6. Program to find the following using math functions:
a.sin 60
b.cos(pi)
c.tan 90
d.angle of sin(0.8660254037844386)
e.5^8
f.square root of 400
g.value of 5^e
h.value of log(1024), base 2
i.value of log(1024), base 10
j.floor and ceiling values of 23.56
k.In [24]:
"""

import math
print("Sine 60=",math.sin(60))
print("Cos pi=",math.cos(math.pi))
print("Tan 90=",math.tan(90))
print("Angle  sin 0.8660254037844386=",math.sin(0.8660254037844386))
print("5^8=",math.pow(5,8))
print("Square root of 400=",math.sqrt(400))
print("The value of 5^e=",math.pow(5,math.e))
print("Log(1024), base 2=",math.log(1024,2))
print("Log(1024), base 10=",math.log(1024,10))
print("Floor of 23.56=",math.floor(23.56))
print("Ceiling of 23.56=",math.ceil(23.56))