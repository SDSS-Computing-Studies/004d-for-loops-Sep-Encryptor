#!python3

"""
##### Problem 2
Calculate the factorial of a number. 

 4! does not mean 4 is excited, it's the notation for a factorial.
A factorial is a special operation in math that is used in probability 
and combination problems.  For example, if you have 4 people, the number
of ways that they can be lined up against the wall is 4!

A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

Note that a factorial can only accept an integer as an input number.  
Your program should also include some "input validation". This means that
the program will only determine the factorial IF the input is a positive
integer.  If the number is not a positive integer, it will display 
"Invalid input"

inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer
Invalid input

example:
Enter a number: 4
4! is 24

example:
Enter a number: -4
Invalid input
"""

N=(input("input a number: ")).strip()
N=int(N)
C=N
a=1
for i in range(0,N):
    a *= N
    N -= 1
a=str(a)
C=str(C)
print(C+"!"+" is "+a)


