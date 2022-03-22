T = int(input())

for i in range(1, T + 1):

	N, B = tuple(map(int, input().split()))
	houses = list(map(int, input().split()))

	houses.sort()

	num_houses = 0

	for house in houses:
		if house <= B:
			num_houses += 1
			B -= house

	print(f'Case #{i}: {num_houses}')

