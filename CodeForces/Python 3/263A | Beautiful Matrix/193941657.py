matrix1 = input()
matrix2 = input()
matrix3 = input()
matrix4 = input()
matrix5 = input()
 
complete_list = []
where = 0
for n in matrix1.split():
    complete_list.append(n)
 
for n in matrix2.split():
    complete_list.append(n)
 
for n in matrix3.split():
    complete_list.append(n)
 
for n in matrix4.split():
    complete_list.append(n)
 
for n in matrix5.split():
    complete_list.append(n)
 
for i in range(len(complete_list)):
    if complete_list[i] == "1":
        where += i
 
moves = 0
 
if where <= 4:
    where += 10
    moves += 2
elif where > 4 and where < 10:
    where += 5
    moves += 1
elif where > 14 and where < 20:
    where -= 5
    moves += 1
elif where >= 20:
    where -= 10
    moves += 2
 
if where == 10:
    moves += 2
if where == 11:
    moves += 1
if where == 13:
    moves += 1
if where == 14:
    moves += 2
print(moves)