# Addition of numbers
num1 = 100
num2 = 200

out = num1 + num2
print(out)

# Addition of number and string 
# num1 = "100"
# num2 = 200

# out = num1 + num2
# print(out)     # Through  TypeError error

# Converting string into numeric
A = "15"
B = "24"

out = int(A)+ int(B)
print(out)

A = "15.5"
B = "24.5"

out = float(A)+ float(B)
print(out)

A = "15"
B = "24.5"

out = int(A)+ int(float(B))
print(out)

# adding list and int
A = [15]
B = 24

out = A[0]+ B

print(out)
