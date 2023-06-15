A, B, C = map(int, input().split())
if A == B == C:
	prize = 10000 + A * 1000
elif A == B or B == C:
	prize = 1000 + B * 100
elif A == C:
	prize = 1000 + A * 100
else:
	if A > B and A > C:
		prize = A * 100
	elif B > A and B > C:
		prize = B * 100
	elif C > B and C > A:
		prize = C * 100

print(prize)