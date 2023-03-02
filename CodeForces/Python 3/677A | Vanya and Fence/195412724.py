friends_and_height = input()
individual_height = input()
friends = int(friends_and_height.split()[0])
fenceheight = int(friends_and_height.split()[1])
height_list = individual_height.split()
 
answer = 0
for h in height_list:
    if int(h) > fenceheight:
        answer += 2
    else:
        answer += 1
 
print(answer)