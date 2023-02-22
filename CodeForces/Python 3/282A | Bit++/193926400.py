lines = int(input())
X = 0
for l in range(lines):
    operation = input()
    for c in operation:
        if c == "-":
            X -= 1
        if c == "+":
            X += 1
 
print(int(X/2))