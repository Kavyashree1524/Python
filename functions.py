# function is a re usable block of code to perform sepecfic task

def greet(user):
    print("\n" *3 + "*"*40)
    print(f"Welcome {user} to ITD")
    print("*"*40)

user1 = "Kavyashee"
greet(user1)

user2 = "Prathiksha"
greet(user2)

def square(num = 4):
    out = num * num
    print(out)
square()

def square(num): #arugment #defining
    return num * num
print(square(5)) # pass paramaters # invocaton / calling

def square(num):
    out = num * num
    return out
print(square(6))

def add(numbers):
    out = 0
    for i in numbers:
        out += i            
    return out
out = add ([10,20,30]) 
print(out)



