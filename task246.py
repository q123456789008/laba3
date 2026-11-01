number = int(input("Enter a positive integer: "))

factorial = 1
for factor in range(2, number + 1):
    factorial *= factor

print(factorial)
