n_k = input()
n = int(n_k.split()[0])
k = int(n_k.split()[1])
 
for i in range(k):
    if n % 10 > 0:
        n -= 1
    else:
        n = n // 10
 
print(n)