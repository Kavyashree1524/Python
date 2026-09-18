#Write a program to check whether a number is positive or negative.

number = int(input("Enter the number: "))

if number>= 1:
    print(f"Entered number {number} is Positive")
elif number == 0:
    print(f"Entered number {number} is Zero")
else:
    print(f"Entered number {number} is Negative")    