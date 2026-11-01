number = input("Enter the number: ")
repeats = int(input("Enter how many times to repeat: "))

numbers = []
for _ in range(repeats):
    numbers.append(number)

print(" ".join(numbers))
