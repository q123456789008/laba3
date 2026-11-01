total = 0
squares_sum = 0

while True:
    number = int(input("Enter a number: "))
    total += number
    squares_sum += number ** 2
    if total == 0:
        break

print(squares_sum)
