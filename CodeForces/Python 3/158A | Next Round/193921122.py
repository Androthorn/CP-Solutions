n_k = input()
separated = n_k.split()
n = separated[0]
k = separated[1]
 
scores = input()
individual_scores = scores.split()
 
advanced = 0
resposta = []
compare = int(k) -1
for i in range(len(individual_scores)):
    if int(individual_scores[i]) >= int(individual_scores[compare]) and int(individual_scores[i]) > 0:
        advanced += 1
 
print(advanced)