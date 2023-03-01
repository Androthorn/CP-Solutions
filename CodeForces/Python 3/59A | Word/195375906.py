def checkupper(letter):
    if ord(letter) < 96:
        return True
    return False
 
word = input()
upper = 0
lower = 0
for letter in word:
    if checkupper(letter):
       upper += 1
    else:
        lower += 1
 
 
if lower > upper or lower == upper:
    print(word.lower())
else:
    print(word.upper())