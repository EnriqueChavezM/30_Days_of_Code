"""
Objective
    Today, we are learning about an algorithmic concept called recursion.

Recursive Method for Calculating Factorial

    factorial(n) = n * factorial(n - 1) n <= 1
    n! = n * (n - 1) * (n - 2) * ... * 1

Function Description
    Complete the factorial function in the editor below. Be sure to use recursion.
    factorial has the following paramter:
        int n: an integer

Returns
    int: the factorial of n
    Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

Input Format
    A single integer, n (the argument to pass to factorial).

Constraints
    2 <= n <= 12
    Your submission must contain a recursive function named factorial.

Initial Code
    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
#Troubleshooting
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)
    print(result)  # Print the result instead of writing to a file

   # fptr.write(str(result) + '\n')

    #fptr.close()