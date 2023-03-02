children_and_seconds = input()
n_of_children = int(children_and_seconds.split()[0])
seconds = int(children_and_seconds.split()[1])
 
boy_or_girl = input()
lista = []
for c in boy_or_girl:
    lista.append(c)
 
def switcharoo(lista):
    i = 0
    while i < len(lista) -1:
        if lista[i] == "B" and lista[i+1] == "G":
            lista[i], lista[i +1] = "G", "B" 
            i += 1
        i += 1        
    return lista
 
for t in range(seconds):
    switcharoo(lista)
 
answer = ""
for letter in lista:
    answer += letter
 
print(answer)