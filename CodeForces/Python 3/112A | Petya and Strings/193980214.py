str1 = input().lower()
str2 = input().lower()
 
result = 0
for c in range(len(str1)):
    if str1[c] > str2[c]:
        result += 1
        break
    if str1[c] < str2[c]:
        result -= 1
        break
print(result)