"""
Objective
    Today, we're working with binary numbers.

Task
    Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

Example
    n = 125
    The binary representation of 125 is 1111101. In base 2, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

Input Format
    A single integer, n.

Constraints
    1 <= n <= 10^6

Output Format
    Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

Initial Code
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    if __name__ == '__main__':
        n = int(input().strip())

"""
#Troubleshooting
#!/bin/python3

import math
import os
import random
import re
import sys

def cambiobase (n):
    x = n // 2
    y = n % 2
    if x == 0:
        return str(y)
    else:
        return cambiobase(x) + str(y)  

def conteo (*arr):
    c = 0
    c1 = []
    for arr in arr:
        if arr == "1":
            c += 1

        else:
            c = 0
        c1.insert(0, c)
        c1.sort()
        c1.reverse()    
    return c1

if __name__ == '__main__':
    #n = int(input("Ingrese un número base 10: ").strip())
    n = int(input().strip())
    arr = list(cambiobase(n))
    valor = int(conteo(*arr)[0])
    """  
    print("El número en base 2 es: " + ''.join(arr))
    print("El número de unos en la representación binaria es: " + str(conteo(*arr)))
    print("La cantidad máxima de unos consecutivos es: " + str(valor))
    """
    print(str(valor))
