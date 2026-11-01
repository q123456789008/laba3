subjects_count = int(input("Enter the number of subjects: "))

total = 0
for number in range(1, subjects_count + 1):
    total += int(input(f"Enter mark {number}: "))

print(f"{total / subjects_count:.2f}")
