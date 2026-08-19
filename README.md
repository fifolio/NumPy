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
