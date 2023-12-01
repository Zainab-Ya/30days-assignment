#exercise level 2
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3%4)
print(3//4)

str_name ="Ado Musa"
print(str_name)
family_name="Ali Sada"
print(family_name)
print('Nigeria')
# Exercise: Level 3
# no. 1
x = 20 #integer
print(type(x))
y = 34 #integer
print(type(y))
a=23.9 #float
print(type(a))
z=10+4j #complex
print(type(z))
my_name='Mukhtar Ado' #sting
print(my_name)
y = (20 +10)>5 #boolean
print(y)
w = 10<4 #boolean
print(w)
Names =['sani','mukhtar','Ado'] #list
print(Names)
print(type({'Name':'Ado', 'class':5})) #dictionary
print(type({2,4,5,6.5,5.5})) #sets
print(type((2,4,6,8.9))) #tuple
#CALCULATING EUCLIDEAN DISTANCE
import math

x1, y1 = 2, 3  # coordinates of the first point
x2, y2 = 10, 8  # coordinates of the second point

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance)