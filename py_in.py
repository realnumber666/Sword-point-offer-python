import sys 
'''

'''
s = sys.stdin.readline().strip()
temp = ''
res = ''
l = []
for c in s:
    if c == '.' or c == '/':
        l.append(temp)
        temp += c
        temp = ''
    temp = temp + c

for i in range(len(l) - 1):
    res += l[len(l) - 1 - i]
print(res)