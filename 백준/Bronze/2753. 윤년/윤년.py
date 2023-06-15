year = int(input())

A = 0

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        A = 1

print(A)