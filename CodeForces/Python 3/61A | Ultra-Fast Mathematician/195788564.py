number_one = input()
number_two = input()
 
def math_conversion(n_1, n_2):
    answer = ""
    for digit in range(len(n_1)):
        if n_1[digit] == n_2[digit]:
            answer += "0"
        else:
            answer += "1"
    return answer
 
print(math_conversion(number_one, number_two))