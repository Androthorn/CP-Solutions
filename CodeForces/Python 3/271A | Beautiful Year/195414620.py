previous_year = int(input())
 
def is_it_distinct(year):
    while True:
        existing_numbers = []
        year += 1
        for digit in str(year):
            if digit not in existing_numbers:
                existing_numbers.append(digit)
        if len(existing_numbers) == 4:
            answer = ""
            for digit in existing_numbers:
                answer += str(digit)
            return answer
 
 
 
print(is_it_distinct(previous_year))