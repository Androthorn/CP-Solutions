n_of_games = int(input())
who_won = input()
anton = 0
danik = 0
for winner in who_won:
    if winner == "A":
        anton += 1
    else:
        danik += 1
 
if anton > danik:
    print("Anton")
elif anton == danik:
    print("Friendship")
else:
    print("Danik")