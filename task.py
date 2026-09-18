# list contains 10 numbers

numbers = [10,20,30,40,50,60,70,80,90,100]
print(len(numbers)) # length of list
print("first: ",numbers[0])
print("last: ",numbers[-1])
print("middle:", numbers[len(numbers)//2])

numbers.append(110) # adding element at the end
print(numbers)

numbers.insert(5,4) # inserting number
print(numbers)

numbers.remove(10) #removing number
print(numbers)

removed =numbers.pop(2) #remove element using index
print("removed element", removed)
print(numbers) 

numbers.reverse() #reverse
print(numbers)

numbers = [3,5,2,9,10]
numbers.sort() #sorting numbers
print("ascending order", numbers)

numbers.sort(reverse = True) # sorting in descending order
print("Descending order", numbers)
