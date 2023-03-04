number_of_magnets = int(input())
 
def do_they_group(list):
    if number_of_magnets == 1:
        return 1
    else:
        grouped = 1
        for i in range(len(list) -1):
            if list[i] != list[i+1]:
                grouped += 1
        return grouped
 
magnets = []
for m in range(number_of_magnets):
    mags = input()
    magnets.append(mags)
 
print(do_they_group(magnets))