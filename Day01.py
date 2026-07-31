"""
Objective
    Today, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

Task
    Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:
    1. Declare 3 variables: one of type int, one of type double, and one of type String.
    2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
    3. Use the + operator to perform the following operations:
        3.1. Print the sum of i plus your int variable on a new line.
        3.2. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
        3.3. Concatenate s with the string you read as input and print the result on a new line.
    Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

Input Format
    The first line contains an integer that you must sum with i.
    The second line contains a double that you must sum with d.
    The third line contains a string that you must concatenate with s.

Output Format
    Print the sum of both integers on the first line, the sum of both doubles (scaled to 1  decimal place) on the second line, and then the two concatenated strings on the third line.

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
"""
# troubleshooting
i = 4
d = 4.0
s = "HackerRank "
# Declare second integer, double, and String variables.
x = int(input())            #12
y = float(input())          #4.0
z = input()                 #is the best place to learn and practice coding!

# Read and save an integer, double, and String to your variables.

suma_i = i + x
suma_d = d + y
concat = s + z

# Print the sum of both integer variables on a new line.
print(suma_i)               # 16

# Print the sum of the double variables on a new line.
print(suma_d)               # 8.0

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(concat)               # HackerRank is the best place to learn and practice coding!
