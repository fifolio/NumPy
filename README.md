## My Personal NumPy Notebook 

What is NumPy?
* NumPy stands for Numerical Python.
* NumPy is a Python library used for working with arrays.
* It also has functions for working in domain of linear algebra, fourier transform, and matrices.

Why Use NumPy?
* In Python we have lists that serve the purpose of arrays, but they are slow to process.
* NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
* The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
* Arrays are very frequently used in data science, where speed and resources are very important.

Why is NumPy Faster Than Lists?
* NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
* This behavior is called locality of reference in computer science.
* This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
* NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

Create a NumPy ndarray Object
* To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray.

Dimensions in Arrays
* A dimension in arrays is one level of array depth (nested arrays).
* nested array: are arrays that have arrays as their elements.

0-D Arrays
* 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

1-D Arrays
* An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.

2-D Arrays
* An array that has 1-D arrays as its elements is called a 2-D array.
* These are often used to represent matrix or 2nd order tensors.

3-D arrays
* An array that has 2-D arrays (matrices) as its elements is called 3-D array.
* These are often used to represent a 3rd order tensor.

Check Number of Dimensions
* NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Higher Dimensional Arrays
* An array can have any number of dimensions.
* When the array is created, you can define the number of dimensions by using the ndmin argument.

Access Array Elements
* Array indexing is the same as accessing an array element.
* You can access an array element by referring to its index number.
* The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

Access 2-D Arrays
* To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
* Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

Access 3-D Arrays
* To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

Negative Indexing
* Use negative indexing to access an array from the end.

NumPy Array Slicing

Slicing arrays

* Slicing in python means taking elements from one given index to another given index.
* We pass slice instead of index like this: [start:end].
* We can also define the step, like this: [start:end:step].
* If we don't pass start its considered 0
* If we don't pass end its considered length of array in that dimension
* If we don't pass step its considered 1

Note: The result includes the start index, but excludes the end index.

Negative Slicing
* Use the minus operator to refer to an index from the end:

STEP
* Use the step value to determine the step of the slicing:

NumPy Data Types

* Below is a list of all data types in NumPy and the characters used to represent them.
* 
* i - integer
* b - boolean
* u - unsigned integer (has no representation for negative numbers.)
* f - float
* c - complex float
* m - timedelta
* M - datetime
* O - object
* S - string
* U - unicode string (dtype="U5"))
* V - fixed chunk of memory for other type ( void )

If you explicitly create a NumPy array with dtype=np.uint8 and put a negative number in it, NumPy wraps the value around rather than storing the negative number.

For example:

```
import numpy as np

x = np.array([-1, 0, 1], dtype=np.uint8)

print(x)
```
You may get:

[255   0   1]

Why does -1 become 255?

Because uint8 can only represent:

0 → 255

So it uses arithmetic modulo 256:

-1 mod 256 = 255

Similarly:

```
np.array([-2, -1, 0, 1], dtype=np.uint8)
```

gives:

[254 255   0   1]

⚠️ Important: this behavior can depend on the NumPy version/context, and newer NumPy versions may raise an OverflowError for direct conversion of a Python negative integer to an unsigned dtype. So don't rely on negative → wraparound when writing new code.

Checking the Data Type of an Array
* The NumPy array object has a property called dtype that returns the data type of the array

* For i, u, f, S and U we can define size as well.

Converting Data Type on Existing Arrays
* The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
* The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
* The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

NumPy Array Copy vs View

The Difference Between Copy and View

* The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
* The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
* The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

- The copy SHOULD NOT be affected by the changes made to the original array.

- The view SHOULD be affected by the changes made to the original array.

- The original array SHOULD be affected by the changes made to the view.

Check if Array Owns its Data

* As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
* Every NumPy array has the attribute base that returns None if the array owns the data.
* Otherwise, the base  attribute refers to the original object.

- The copy returns None.
- The view returns the original array.

