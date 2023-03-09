t = int(input())
answers = []
for x in range(t):
    n = int(input())
    complete_list = ""
    elements_in_each_side = n // 2
    last_odd_element = (n//2) -1 + n
    if n == 2:
        answers.append("NO")
        continue
    elif last_odd_element % 2 == 0:
        answers.append("NO")
        continue
    evens_list = []
    odds_list = []
    evens = 2
    sum_of_evens = 0
    odds = 1
    sum_of_odds = 0
    for index in range(elements_in_each_side):
        if elements_in_each_side > 1 and index == elements_in_each_side -1:
            odds_list.append(last_odd_element)
            sum_of_odds += last_odd_element
            evens_list.append(evens)
            sum_of_evens += evens
        else:
            evens_list.append(evens)
            odds_list.append(odds)
            sum_of_evens += evens
            sum_of_odds += odds
            evens += 2
            odds += 2
    for e in evens_list:
        complete_list += f"{e} "
    for e in odds_list:
        complete_list += f"{e} "    
    answers.append("YES")
    answers.append(complete_list.strip())
 
for x in answers:
    print(x)