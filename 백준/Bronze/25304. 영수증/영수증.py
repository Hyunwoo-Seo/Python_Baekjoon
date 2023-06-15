A = int(input())
B = int(input())

C = 0
for i in range(B):
    D, E = map(int, input().split())
    C += D * E

if C == A:
    print("Yes")
else:
    print("No")