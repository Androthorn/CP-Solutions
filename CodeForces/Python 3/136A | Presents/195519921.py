friends = int(input())
indexes = input()
separated = indexes.split()
 
answer_list = []
for x in range(friends):
    answer_list.append("0")
 
for x in range(friends):
    answer_list[int(separated[x])-1] = x+1
 
answer = ""
for i in range(len(answer_list)):
    if i == -1:
        answer += answer_list[i]
    else:
        answer += f"{answer_list[i]} "
 
print(answer)