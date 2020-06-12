import pygame

pi = 3.14159265359
distance = float(input('Please enter the required distance(cm) : '))
step_angle = float(input('Please enter the necessary step angle : '))
wheel_size = float(input('Please enter the required Diameter(cm) :  '))

circumference = pi * wheel_size
steps = (distance/circumference)*(360/step_angle)
print(steps)
