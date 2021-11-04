#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def generate_random_elements(arr):
    for i in range(10):
        randomItemOfList = random.randint(1, 100)
        arr.append(randomItemOfList)
        i += i
    return arr

print(generate_random_elements(my_list))