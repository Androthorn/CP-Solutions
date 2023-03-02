number_of_rooms = int(input())
available = 0 
 
for x in range(number_of_rooms):
    people_and_capacity = input()
    occupants = int(people_and_capacity.split()[0])
    capacity = int(people_and_capacity.split()[1])
    if capacity - occupants >= 2:
        available += 1
 
print(available)