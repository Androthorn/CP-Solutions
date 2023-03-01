number_of_stops = int(input())
minimum = 0 
minimum_temp = 0
for stops in range(number_of_stops):
    capacity = input()
    out = capacity.split()[0]
    inside = capacity.split()[1]
    if stops == 0:
        minimum_temp += int(inside)
    else:
        minimum_temp -= int(out)
        minimum_temp += int(inside)
    if minimum_temp > minimum:
        minimum = minimum_temp
 
print(minimum)