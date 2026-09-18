# import os

# for file in os.listdir("."):
#     print(file) 

#Print numbers from 1 to 20 using a for loop.

# for i in range (1 , 21):
#     print(i)

for i in range (1, 100):
    if i == 21:
        break
    print(i)

#Print numbers from 20 to 1 using a while loop.

count = 20
while count >= 1:
    print(count)
    count -= 1

#Print all even numbers from 1 to 50.
for i in range (2, 51, 2):
    print(i)
 #or
for i in range (1, 50):
    if i%2 == 0:
        print(i)  

#Print all odd numbers from 1 to 50.
  