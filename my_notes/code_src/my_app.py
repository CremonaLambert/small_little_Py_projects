# name = input('Hey!...What is your name?\n')
# print('Nice to meet you' + ' ' + name)


#-------How to work with strings--------------

# first_name = 'Cremona'
# surname = 'Mwinkeu'

# full_name = first_name + ' '+ surname
# print(full_name.endswith('eu'))

# print(len(first_name))


#------How to work With numbers-----------------

# addition = 15 + 17 
# print(addition)

# substraction = 170 - 150
# print(substraction)

# multiplication = 50 * 2
# print(multiplication)

# division = 350 / 50
# print(division)

# modulus = 12 % 5
# print(modulus)

# a = 100
# b = 200
# c = a + b 
# print('the sum of {} and {} gives {}'.format(a, b, c))

# numbers = 156
# if numbers % 2 == 0:
#     print('this number is even')
# else:
#     print('this number is odd')


#--------How to work with boolean-----

# ten = 10
# two = 2
# print(two > ten)   # false


# print( ten >= (20/two))  #true

# print('cremona'.endswith('a'))  #true


#-------if statements--------------- it controles the flow of our programme

# age = 5
# if age >= 18 & age <= 59 :
#     print('this guy is an adult')
# if age > 60:
#     print('aah! this guy is very old')
# if age <= 17 :
#     print('take this guy out he is under age')

# --------How to work with lists----------------------------

# cars = ['bmw', 'tesla', 'mercedes']
# print(len(cars))
# print(cars[0:2])

#------------How to work with for loops------------------

# cars = ['bmw', 'tesla', 'mercedes', 'toyota', 'isuzu']

# # for car in cars:
# #     print(car)

# for car in cars:       # loop through cars
#     if car == 'toyota':    # if the car is equal to toyota
#         print(car.upper())     # upper case everthing
# else:
#     print(car.capitalize())    #othewise capitalize the first caractor


#--------How to work with while loops -------------------

# number = 0
# while number <= 10:
#     print(number)
#     number = number + 2


# ---------How to use Functions --------------------

# def ckech_age(age):
#     if age < 18:
#         print('oops not an adult')
#     else:
#         print('hooray I am an adult')
# ckech_age(18)
# ckech_age(8)
# ckech_age(100)
# ckech_age(50)

# -----How to work with built in functions-------------

# print('cremona'.startswith('c'))

# -----How do we work with propertie of classes --------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# cremona = Person('Cremona', 29)
# arlette = Person ('Arlette', 26)

# print(cremona.name+ ' is ' +str(cremona.age))
# print(arlette.name+ ' is ' +str(arlette.age))


# --------How to work with classes and behaviors and objects--------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name + ' '+ 'is walking...')
    

    def speak(self):
        print('Hello my name is'+' '+ self.name+ ' '+ 'and i am'+ ' '+str(self.age)+ ' '+ 'years old')
cremona = Person('Cremona', 29)
arlette = Person ('Arlette', 26)

print(cremona.name+ ' is ' +str(cremona.age))
cremona.speak()
cremona.walk()


print(arlette.name+ ' is ' +str(arlette.age))
arlette.speak()
arlette.walk()


