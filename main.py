
# ******************************
# Make your Code
# ******************************
numbers = []

for i in range(5):
    numbers.append(int(input()))

avg = sum(numbers) / len(numbers)

for n in numbers:
    if n > avg:
        print(n, end=" ")
