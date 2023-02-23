limak_and_bob_weights = input()
 
limak_weight = int(limak_and_bob_weights.split()[0])
bob_weight = int(limak_and_bob_weights.split()[1])
 
years = 0
while True:
    years += 1
    limak_weight *= 3
    bob_weight *= 2
    if limak_weight > bob_weight: break
 
print(years)