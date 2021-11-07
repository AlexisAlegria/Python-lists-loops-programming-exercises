import random

def matrixBuilder(num):
    matrix = []
    items_of_matrix = []
    
    for i in range(1, num + 1):
        matrix.append(items_of_matrix)
    
    for j in matrix:
        items_of_matrix.append(1)
    return matrix

print(matrixBuilder(7))