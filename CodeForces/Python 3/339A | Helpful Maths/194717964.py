entry = input()
individual_numbers = entry.split("+")
individual_numbers.sort()
 
 
answer = ""
for i in range(len(individual_numbers)):
    if i == 0:
        answer += individual_numbers[0]
    else:
        answer += f"+{individual_numbers[i]}"
 
print(answer)