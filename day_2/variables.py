# Exercise level1
# Day 2: 30 Days of python programming
first_name = "Adamu"
last_name ="Sani"
full_name = "Adamu Sani "
country ="Nigeria"
city="kano"
Age=30
year=2023
is_married=True
is_true=False
is_light_on = 'Yes'
first_name, last_name,country,Age='Adamu','Sani','Nigeria',30

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(Age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))
num_one=5
num_two=4
total=num_one + num_two
print(total)
diff=num_two - num_one
print(diff)
product=num_two * num_one
print(product)
division=num_one / num_two
print(division)
reminder=num_two % num_one
print(reminder)
exp=num_one ** num_two
print(exp)
floor_division=num_one//num_two
print(floor_division)
 
#calculating radius of a circle
import math
radius=30
_area_of_circle_=  math.pi * (radius**2)
print(_area_of_circle_)

#calculating circumference of a circle
_circum_of_circle_= 2*math.pi*radius
print(_circum_of_circle_)

#using radius as input
radius=input('enter radius:')
print(_area_of_circle_)

#using built_in functions
first_name = input('first name:')
print(first_name)
last_name = input('enter last name:')
print(last_name)
country = input('enter your country:')
print(country)
age=input('enter your age:')
print(age)

help()