# finding
Searching a 2D ndarray for a given value and finding values in area 'near' to that value.


A 2D array is generated with A = np.random.random((N, N, 1))*100
In general it should work on n-D arrays and not only containing 1 value as elements.

It should be possible to find a value which is closest to <X> and display its 
coordinates/index.

Example:

2D 3x3 matrix:

1  2  5
6  2  1
3  4  3

In a basic mode the function "get_value(X)" should return 5 if X=5. Also it 
should be able to display coordinates like: index=[0, 3] (in case of this matrix).
