k_n_w = input()
k = int(k_n_w.split()[0])
n = int(k_n_w.split()[1])
w = int(k_n_w.split()[2])
 
total = 0
for x in range(1,   w +1):
    total += k * x
 
borrows = total - n
 
if borrows > 0:
    print(borrows)
else:
    print(0)