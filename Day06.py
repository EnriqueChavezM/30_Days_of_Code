"""
Objective
    Today we will expand our knowledge of strings, combining it with what we have already learned about loops.

Task
    Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.
    Note: 0 is considered to be an even index.

Example
    S = adbecf
    Print abc def

Input Format
    The first line contains an integer, T (the number of test cases).
    Each line i of the T subsequent lines contain a string, S.

Constraints
    1 <= T <= 10
    2 <= length of S <= 10000

Output Format
    For each String Sj (where 0 <= j <= T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters, separated by a space.

Initial Code
    # Enter your code here. Read input from STDIN. Print output to STDOUT
"""
#Troubleshooting
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    T = int(input().strip())
    for i in range(T):
        S = input().strip()
        even_chars = S[::2]  # Characters at even indices
        odd_chars = S[1::2]  # Characters at odd indices
        print(f"{even_chars} {odd_chars}")