number_of_drinks = int(input())
percentage_of_orange_per_drink = input()
list_of_percentages = percentage_of_orange_per_drink.split()
 
def how_much_orange(list):
    divisor = len(list) * 100
    dividend = 0
    for n in list:
        dividend += float(n)
    return dividend / divisor * 100
 
 
print(f"{how_much_orange(list_of_percentages):.12f}")