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

NumPy Array Shape

Shape of an Array
* The shape of an array is the number of elements in each dimension

Get the Shape of an Array
* NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

NumPy Array Reshaping

Reshaping arrays
* Reshaping means changing the shape of an array.
* The shape of an array is the number of elements in each dimension.
* By reshaping we can add or remove dimensions or change number of elements in each dimension.

Can We Reshape Into any Shape?
* Yes, as long as the elements required for reshaping are equal in both shapes.
* We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

Unknown Dimension

* You are allowed to have one "unknown" dimension.
* Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
* Pass -1 as the value, and NumPy will calculate this number for you
* Note: We can not pass -1 to more than one dimension.

Flattening the arrays
* Flattening array means converting a multidimensional array into a 1D array.
* We can use reshape(-1) to do this.
* Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.

NumPy Array Iterating

Iterating Arrays

* Iterating means going through elements one by one.*
* As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.*
* If we iterate on a 1-D array it will go through each element one by one.
* In a 2-D array it will go through all the rows.

Iterating Arrays Using nditer()

* The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration,

Iterating Array With Different Data Types

* We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
* NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

Iterating With Different Step Size
* We can use filtering and followed by iteration.

Enumerated Iteration Using ndenumerate()
* Enumeration means mentioning sequence number of somethings one by one.
* Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

NumPy Joining Array

* Joining means putting contents of two or more arrays in a single array.
* In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
* We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

Joining Arrays Using Stack Functions

* Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
* We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
* We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
* NumPy provides a helper function: hstack() to stack along rows.
* NumPy provides a helper function: vstack()  to stack along columns.
* NumPy provides a helper function: dstack() to stack along height, which is the same as depth.


NumPy Splitting Array

* Splitting NumPy Arrays
* Splitting is reverse operation of Joining.
* Joining merges multiple arrays into one and Splitting breaks one array into multiple.
* We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
* If the array has less elements than required, it will adjust from the end accordingly.
* Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

Split Into Arrays
* The return value of the array_split() method is a list containing each of the split as an array.
* If you split an array into 3 arrays, you can access them from the result just like any array element.

Splitting 2-D Arrays
* Use the same syntax when splitting 2-D arrays.
* Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
* Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().

NumPy Searching Arrays

Searching Arrays
* You can search an array for a certain value, and return the indexes that get a match.
* To search an array, use the where() method.

Search Sorted
* There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
* The searchsorted() method is assumed to be used on sorted arrays.
* By default the left most index is returned, but we can give side='right' to return the right most index instead.

Multiple Values
* To search for more than one value, use an array with the specified values.

NumPy Sorting Arrays

Sorting Arrays
* Sorting means putting elements in an ordered sequence.
* Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
* The NumPy ndarray object has a function called sort(), that will sort a specified array.
* Note: This method returns a copy of the array, leaving the original array unchanged.
* You can also sort arrays of strings, or any other data type.

NumPy Filter Array

Filtering Arrays
* Getting some elements out of an existing array and creating a new array out of them is called filtering.
* In NumPy, you filter an array using a boolean index list.
* A boolean index list is a list of booleans corresponding to indexes in the array.
* If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

Random Numbers in NumPy

Generate Random Number
* NumPy offers the random module to work with random numbers.

Generate Random Float
* The random module's rand() method returns a random float between 0 and 1.

Generate Random Array
* In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

Integers
* The randint() method takes a size parameter where you can specify the shape of an array.

Floats
* The rand() method also allows you to specify the shape of the array.

Generate Random Number From Array
* The choice() method allows you to generate a random value based on an array of values.
* The choice() method takes an array as a parameter and randomly returns one of the values.
* Add a size parameter to specify the shape of the array.

Random Data Distribution

* What is Data Distribution?
* Data Distribution is a list of all possible values, and how often each value occurs.
* Such lists are important when working with statistics and data science.
* The random module offer methods that returns randomly generated data distributions.

Random Distribution

* A random distribution is a set of random numbers that follow a certain probability density function.
* Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.
* We can generate random numbers based on defined probabilities using the choice() method of the random module.
* The choice() method allows us to specify the probability for each value.
* The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.
* The sum of all probability numbers should be 1.

Random Permutations

Random Permutations of Elements
* A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
* The NumPy Random module provides two methods for this: shuffle() and permutation().

Shuffling Arrays
* Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
* The shuffle() method makes changes to the original array.

* The permutation() method returns a re-arranged array (and leaves the original array un-changed).

Seaborn

Displots
* Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

