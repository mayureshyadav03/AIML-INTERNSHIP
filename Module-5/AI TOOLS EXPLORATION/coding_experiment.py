numbers = [10, 15, 20, 25, 30, 35]

average = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("Numbers:", numbers)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Even numbers:", even_count)