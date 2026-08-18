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