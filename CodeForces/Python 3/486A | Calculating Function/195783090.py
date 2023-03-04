number = int(input())
 
def alternating_function(num):
    if num % 2 == 0:
        return  num // 2
    if num % 2 == 1:
        return -((num // 2) + 1)
 
print(alternating_function(number))