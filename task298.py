min_digits = int(input("Enter the minimum number of digits: "))
max_digits = int(input("Enter the maximum number of digits: "))

count = 0
for digits in range(min_digits, max_digits + 1):
    count += 9 * 10 ** (digits - 1)

print(count)
