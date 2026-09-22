import numpy as nm

numbers = nm.array([5, 2, 8, 1, 3])

for i in range(len(numbers)):
	swapped = False

	for j in range(len(numbers) - 1 - i):
		if numbers[j] > numbers[j + 1]:
			numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
			swapped = True

	if not swapped:
		break

print(numbers)

