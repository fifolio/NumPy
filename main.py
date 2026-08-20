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

# Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# Slice elements from index 4 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])

# Slice from the index 3 from the end to index 1 from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])

# Return every other element from index 1 to index 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])

# From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])

# From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 1:4])

# Get the data type of an array object:
arr = np.array([1, 2, 3, 4])
# print(arr.dtype)

# Get the data type of an array containing strings:
arr = np.array(['v1', 'v2', 'v3', 'v4'])
# print(arr.dtype)

# Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)

# A non integer string like 'a' can not be converted to integer (will raise an error):
# arr = np.array(['a', '2', '3'], dtype='i')
# print(arr.dtype)

# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

# print(newarr)
# print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

# print(newarr)
# print(newarr.dtype)

# Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

# print(arr)
# print(x)

# Make a view, change the original array, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

# print(arr)
# print(x)

# Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

# print(arr)
# print(x)

# Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

# print(x.base)
# print(y.base)

# Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape) # The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)