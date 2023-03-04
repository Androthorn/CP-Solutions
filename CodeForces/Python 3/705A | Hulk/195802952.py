number = int(input())
a = "I hate it"
b = "that I love "
c = "that I hate "
answer = "I hate "
lista = []
 
if number == 1:
    print(a)
else:
    for x in range(2, number +1):
        lista.append(x)
    for x in range(len(lista)):
        if int(x) % 2 == 0:
            answer += b
        if int(x) % 2 == 1:
            answer += c
 
    answer += "it"
 
    print(answer)