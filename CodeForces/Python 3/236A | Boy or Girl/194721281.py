nickname = input()
letters_present = []
 
for letter in nickname:
    if letter not in letters_present:
        letters_present.append(letter)
 
counter = 0
for letter in letters_present:
    counter += 1
 
if counter % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")