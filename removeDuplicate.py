# # Remove Duplicate Characters from a String Input: programming output: progamin

name = "programming"
result = ""

for characters in name :
    if characters not in result:
        result += characters

print("Output:", result)


