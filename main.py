import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

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

# print(arr)
# print('shape of array :', arr.shape)

# Convert the following 1-D array with 12 elements into a 2-D array. The outermost dimension will have 4 arrays, each with 3 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

# print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array. The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

# print(newarr)

# Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base) # The example above returns the original array, so it is a view.

# Convert 1D array with 8 elements to 3D array with 2x2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 1, -1)

# print(newarr)

# Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

# print(newarr)

# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3, 4, 5])
for el in arr:
    # print(el)
    break

# Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for el in arr:
# print(el) # If we iterate on a n-D array it will go through n-1th dimension one by one.
  break

# Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)

# Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   print(x)

# Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)

# Iterate through the following 3-D array Using nditer():
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)

# Iterate through the array as a string:
arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr[:, ::2]):
#   print(x)

# Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# Enumerate on following 2D array's elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# Join two arrays:
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

# Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

# print(arr)

# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

# print(arr)

# NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

# print(arr)

# NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

# print(arr)

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

# print(arr)

# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

# print(newarr) # Note: The return value is a list containing three arrays.

# Split the array in 4 parts:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

# print(newarr)

# Access the splitted arrays:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

# print(newarr) # The example above returns three 2-D arrays.

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

# print(newarr)

# Split the 2-D array into three 2-D arrays along columns.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

# print(newarr)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

# print(newarr)

# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

# print(x)

# Find the indexes where the values are odd:
arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr%2 == 1)

# print(x)

# Find the indexes where the values are even:
arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr%2 == 0)

# print(x)

# Find the indexes where the value 7 should be inserted:
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

# print(x) # The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

# Find the indexes where the value 7 should be inserted, starting from the right:
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

# print(x) 

# Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

# print(x)

# Sort the array:
arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))

# Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])

# print(np.sort(arr))

# Sort a boolean array:
arr = np.array([True, False, True])

# print(np.sort(arr))

# If you use the sort() method on a 2-D array, both arrays will be sorted:
arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))

# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

# print(newarr)

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# Generate a random integer from 0 to 100:
x = random.randint(100)

# print(x)

# Generate a random float from 0 to 1:
x = random.rand()

# print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100:
x = random.randint(100, size=(5))

# print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))

# print(x)

# Generate a 1-D array containing 5 random floats:
x = random.rand(5)

# print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)

# print(x)

# Return one of the values in an array:
x = random.choice([3, 5, 7, 9])

# print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))

# print(x)

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.3, 0.3], size=(100))

# print(x)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

# print(x)

# Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

# print(arr)

# Generate a random permutation of elements of following array:
arr = np.array([1, 2, 3, 4, 5])

# print(random.permutation(arr))

sns.displot([0, 1, 2, 3, 4, 5])
# plt.savefig("plot.png")

# Generate a random normal distribution of size 2x3:
x = random.normal(size=(2, 3))
# print(x)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)

# Visualization of Normal Distribution
sns.displot(random.normal(size=1000), kind="kde")
# plt.savefig("Visualization of Normal Distribution.png")

# Given 10 trials for coin toss generate 10 data points:
x = random.binomial(n=10, p=0.5, size=10)

# print(x)

# Visualization of Binomial Distribution
sns.displot(random.binomial(n=10, p=0.5, size=1000))

# plt.savefig("Visualization of Binomial Distribution.png")

# Difference Between Normal and Binomial Distribution

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

# plt.savefig("normal-binomial.png")

# Generate a random 1x10 distribution for occurrence 2:
x = random.poisson(lam=2, size=10)

# print(x)

# Visualization of Poisson Distribution
sns.displot(random.poisson(lam=2, size=1000))

# plt.savefig("Poisson Distribution.png")

# Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
# print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

# print(z)
