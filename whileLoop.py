"""while <until_condition_true> : contorl the loop based on the condition
    statement
    statement"""

counter = 0
while counter < 3: 
    counter += 1
    print(counter)

counter1 =0
something = True

while something:
    counter1 += 1
    print(counter1)
    if counter1 == 5:
     something = False

number = [2,4,5,6,8,10]
while number:
    out = number.pop()

    print(out ** 2)
print(number)