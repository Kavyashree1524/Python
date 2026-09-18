#Write a program to check whether a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if age>= 18:
    print(f"Your age is {age}, You are Eligible for Vote")
else:
    print(f"Your age is {age}, You are not Eligible for Vote")