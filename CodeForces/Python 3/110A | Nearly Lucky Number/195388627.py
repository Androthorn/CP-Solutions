n = int(input())
 
lucky = 0
for number in str(n):
    if number == "7" or number == "4":
        lucky += 1
 
if lucky == 4 or lucky == 7:
    print('YES')
else:
    print("NO")