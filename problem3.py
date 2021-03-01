#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

N=input(("enter a integer: ")).strip()
N=input(N)
a=0
for i in range(0,N):
    c="1"*N
    c=int(c)
    a += c
    N -= 1
a=str(a)
print("the sum of the series is "+a)
