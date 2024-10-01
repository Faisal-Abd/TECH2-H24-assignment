"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np

num_lst = [1, 2, 3, 4, 5,]

def std_loops(num_lst):
    total_sum = 0
    total_num = 0
    mean = 0
    #Adds total sum and total numbers of a sequence by looping until all elements in the given list has been used. 
    for i in num_lst:
        total_sum += i
        total_num += 1
    # mean = average of the sequence
    mean = total_sum/total_num

    sumOfSquares = 0
    #Iterates each element in the list and subtracts by mean first, then squares it, while also adding each iteration.
    for i in num_lst:
        sumOfSquares += (i - mean) ** 2
    #variance is the sum of the squared numbers divided by the total number of elements in the sequence.
    variance = sumOfSquares/total_num
    #Get standard deviation (sd) by taking the square root (or to the power of 0.5) of the variance.   
    sd = (variance) ** 0.5
    return (sd)    
print(std_loops(num_lst))

#Using builtin sum() and len()
def std_builtin(num_lst):
    # sumOfNum = total sum of a sequence using sum()
    sumOfNum = sum(num_lst)
    # n = total length of a sequence using len()
    n = len(num_lst)
    # mean = average of a sequence
    average = sumOfNum/n
    # sumOfSquares is the sum of each element subtracted by the average to the power of 2.
    sumOfSquares = sum((i - average) ** 2 for i in num_lst)
    # variance is the sum of the squared numbers divided by the total number of elements in the sequence.
    variance = sumOfSquares/n
    # sd = standard deviation 
    sd = variance**0.5

    return (sd)

print(std_builtin(num_lst))

#Using NumPy function std()
def numpyStd(num_lst):
    sd = np.std(num_lst)
    return sd
print(numpyStd(num_lst))