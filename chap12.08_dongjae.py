s = input()
alpha = []
total = 0
result = ''
for x in s:
    if x.isalpha():
        alpha.append(x)
    else:
        total += int(x)
alpha.sort()
alpha.append(str(total))
for x in alpha:
    result += x
print(result)
