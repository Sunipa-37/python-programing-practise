s1 = input().strip()
s2 = input().strip()

result = ""

n = min(len(s1), len(s2))

for k in range(n):
    result += s1[k]
    result += s2[-(k+1)]

if len(s1) > n:
    result += s1[n:]
if len(s2) > n:
    leftover = s2[0:len(s2)-n]
    result += leftover[::-1]

print(result)

