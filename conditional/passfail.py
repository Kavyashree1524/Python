# Write a program to determine whether a student has passed (marks >= 35).

marks = int(input("Enter your marks: "))

if marks >= 35:
    print(f"Student has passed with {marks} marks")
else:
    print(f"Student has failed with {marks} marks")