num = int(input("Enter a number: "))
total = 0

for digit in str(num):
    total = total + int(digit)

print("Sum of digits =", total)