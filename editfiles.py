import re

'''with open('que.txt', 'r') as firsttext:
    lines = firsttext.readlines()
    print(lines)

for i in range(len(lines)):
    var = re.match(r'\d{,3}\W', lines[i])
    lines[i] = re.sub(var.group(), (str(i + 1) + '.'), lines[i])

with open('q.txt', 'w') as finaltext:
    finaltext.writelines(lines)
'''
with open('ans.txt', 'r') as firsttext:
    linesA = firsttext.readlines()
    print(linesA)

count = 1
for i in range(len(linesA)):
    if '***' in linesA[i]:
        var = re.match(r'\d{,3}', linesA[i])
        linesA[i] = re.sub(var.group(), str(count), linesA[i])
        count += 1

with open('a.txt', 'w') as finaltext:
    finaltext.writelines(linesA)