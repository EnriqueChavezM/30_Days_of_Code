"""
Objective
    Today, we are building on our knowledge of arrays by adding another dimension. 

Context
    Given a 6 x 6 2D Array, :

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

    a b c
      d
    e f g
    There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
    Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example

        In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format

    There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints
    -9 <= A[i][j] <= 9
    0 <= i,j <= 5

Output Format
    Print the maximum hourglass sum in A.

Initial Code
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    if __name__ == '__main__':
        arr = []
        for _ in range(6):
            arr.append(list(map(int, input().rstrip().split())))
"""
#This ia a solution
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    # Read the 6x6 matrix
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # List to store all hourglass sums
    hourglass_sums = []

    # Iterate over possible positions
    for i in range(4):          # rows 0 to 3
        for j in range(4):      # columns 0 to 3
            # Calculate the hourglass sum
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total = top + middle + bottom

            hourglass_sums.append(total)

    # Print all hourglass sums
    print("All hourglass sums:", hourglass_sums)

    # Print the maximum sum
    print("Maximum sum:", max(hourglass_sums))