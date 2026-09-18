"""Count Word Frequency in a Sentence
Input: apple banana apple orange banana apple
output: apple : 3 banana : 2 orange : 1"""

sentence = input("Enter a sentence: ")
words = sentence.split()
frequency ={} 

for word in words: #loops trough every word 
    if word in frequency:
        frequency[word] += 1 
    else:    
        frequency[word] = 1 
print(frequency)        
for word, count in frequency.items():
    print(f"{word} : {count}")

