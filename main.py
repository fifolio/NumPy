import numpy as np

# Use a tuple to create a NumPy array:
arr = np.array((1, 2, 3, 4, 5))
# print("Tuple to create a NumPy array: ", arr)

# Create a 0-D array with value 42
arr = np.array(42)
# print("0-D array: ", arr)

# Create a NumPy ndarray Object (1-D array)
arr = np.array([1, 2, 3, 4, 5])
# print("1-D array: ", arr)

# 2-D array containing two arrays
arr = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])
# print("2-D array: ", arr)

# 3-D array with two 2-D arrays, both containing two arrays 
arr = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[1, 2, 3], [4, 5, 6]]
    ])
# print("3-D array: ", arr)

# Check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)
# print("In this array the innermost dimension (5th dim) has 4 elements, \n the 4th dim has 1 element that is the vector, \n the 3rd dim has 1 element that is the matrix with the vector, \n the 2nd dim has 1 element that is 3D array \n and 1st dim has 1 element that is a 4D array.")

# Get the first element from the following array:
arr = np.array([1, 2, 3, 4])
# print(arr[0])

# Get the second element from the following array.
arr = np.array([1, 2, 3, 4])
# print(arr[1])

# Get third and fourth elements from the following array and add them.
arr = np.array([1, 2, 3, 4])
# print(arr[2] + arr[3])

# Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])

# Access the element on the 2nd row, 5th column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('5th element on 2nd row: ', arr[1, 4])

# Access the third element of the second array of the first array:
arr = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
    ])
# print(arr[0, 1, 2])

# Print the last element from the 2nd dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])

