#Write function for calculator  which can return the output for 2 numbers with kind of operation provided.

def calculator(a,b,operation):
    if operation == "+" :
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b

print(calculator(10,2,"+"))
print(calculator(10,2,"-"))
print(calculator(10,2,"*"))
print(calculator(10,2,"/"))


# Write function that can return repetitive elements 

def repeat(numbers):
    result = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in result:
            result.append(num)
    return result

print(f"returning repetitive elementes :{repeat([1,2,3,2,4,1])}")