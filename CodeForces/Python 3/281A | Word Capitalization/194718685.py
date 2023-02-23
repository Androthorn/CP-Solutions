word = input()
answer = ""
 
for i in range(len(word)):
    if i == 0:
        answer += word[0].upper()
    else:
        answer += word[i]
 
print(answer)