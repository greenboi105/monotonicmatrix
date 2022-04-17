# monotonicmatrix
Python algorithm that searches for items in a partially sorted matrix.

We define a "row-column monotonic" matrix of numbers as one in which entries increase or remain constant along all rows and columns. 

We want to utilize the fact that the matrix is monotonic to create a function my_search(Q, item) that is more efficient than simply parsing through every possible row and column. 

The program's initial task is to create a class my_float that behaves identically to an ordinary floating-point number but maintains a counter comparison_counter to identify whenever a comparison has been made. When a comparison is made the counter is incremented.

The second task is to generate monotonic matrices using the numpy module and its arrays. The function my_generate_monotonic_matrices takes as parameters a number for the dimensions of the output matrix and returns a square monotonic matrix.

The third task is to implement a function my_search_linear that simply uses a pair of nested for loops to search every element in the matrix for what we want to obtain. This implementation has a worst-case time scenario of O(n^2).

The final task is to implement an improved search function that utilizes that the matrix is sorted by row and column to improve the number of checks that must be performed until we determine if the element is present in the matrix. Although this function also has a worse-case scenario of O(n^2), in the majority of instances its performance will be better than the brute-force implementation.
