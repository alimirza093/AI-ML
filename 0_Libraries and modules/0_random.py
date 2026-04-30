""""Random Module is use to generate random numbers and perform random operations in Python. It provides various functions to generate random numbers, shuffle sequences, and perform other random operations."""


import random

#generate a random number between 10 to 50 and jump 3 numbers
random_number = random.randrange(10 , 50 , 3)
print("Random Number:",random_number,"\n")


#generate a random float number between 0 and 1
random_float = random.random()
print("Random Float:",random_float,"\n")


#generate a random float number between 1.5 and 10.5
random_float_range = random.uniform(1.5 , 10.5)
print("Random Float Range:",random_float_range,"\n")


#generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print("Random Integer:",random_integer,"\n")
# 
