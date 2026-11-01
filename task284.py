largest = 0
largest_count = 0

number = int(input("Enter a number (0 to finish): "))
while number != 0:
    if number > largest:
        largest = number
        largest_count = 1
    elif number == largest:
        largest_count += 1
    number = int(input("Enter a number (0 to finish): "))

print(largest_count)
