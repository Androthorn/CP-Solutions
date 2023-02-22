problems = int(input())
can_do = 0
for p in range(problems):
    solves = input()
    knows = solves.split()
    soma = 0
    for n in knows:
        soma += int(n)
    if soma >= 2:
        can_do += 1
 
print(can_do)