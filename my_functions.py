import numpy as np
import random


class my_float(float):
    comparison_counter = 0

    def __eq__(self, other):
        my_float.comparison_counter += 1
        return super().__eq__(other)
    # Add the other required magic methods
    def __ne__(self, other):
        my_float.comparison_counter += 1
        return super().__ne__(other)

    def __lt__(self, other):
        my_float.comparison_counter += 1
        return super().__lt__(other)
    
    def __gt__(self, other):
        my_float.comparison_counter += 1
        return super().__gt__(other)

    def __le__(self, other):
        my_float.comparison_counter += 1
        return super().__le__(other)

    def __ge__(self, other):
        my_float.comparison_counter += 1
        return super().__ge__(other)

def my_generate_monotonic_matrix(size):

    M = np.full([size, size], int)

    initial_row_value = 0
    for i in range(size):
        for j in range(size):
            gen = random.random()
            change = int(round(gen+1, 1)*10)
            if (i == 0):
                initial_row_value += change
                M[i,j] = initial_row_value
            elif (i != 0 and j == 0):
                M[i,j] = M[i-1,j] + change
            elif (i != 0 and j != 0):
                M[i,j] = max(M[i-1, j], M[i, j-1]) + change
    return M
            

# Do not modify the function generate_monotonic_matrix
def generate_monotonic_matrix(size):
    n = size;
    Q = np.full([n, n], my_float)

    S_row_0 = 0
    for i in range(n):
        for j in range(n):
            delta = random.random()

            if (i == 0):
                S_row_0 += delta
                Q[i, j] = my_float(round(S_row_0, 1))
            elif (i != 0 and j == 0):
                Q[i, j]  = my_float(round(Q[i-1, j] + delta, 1))
            elif (i != 0 and j != 0):
                Q[i, j] = my_float(round(max(Q[i-1, j], Q[i, j-1]) + delta,1))

    return Q

def my_search_linear(Q, item):
    shape = Q.shape
    n = shape[0]
    comparison = my_float(item)
    for i in range(n):
        for j in range(n):
            if comparison.__eq__(Q[i,j]) == True:
                return True
    else:
        return False


def my_search(Q, item):
    j = len(Q) - 1
    for row in Q:
        while row[j] > item:
            j = j - 1
            if j == -1:
                return False
        if row[j] == item:
            return True
    return False
   

floating = my_float(5)

floating.__eq__(float(5.0))