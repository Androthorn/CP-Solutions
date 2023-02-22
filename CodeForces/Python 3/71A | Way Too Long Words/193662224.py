lines = int(input())
answer = []
for l in range(lines):
    word = input()
    if len(word) > 10:
        new = ""
        new += word[0]
        new += str(len(word)-2)
        new += word[-1]
        answer.append(new)
    else:
        answer.append(word)
for w in answer:
    print(w)