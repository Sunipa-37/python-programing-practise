lst = ["apple", "kick", "mango", "like", "king"]
k = input("Enter character: ")

freq = []
for s in lst:
    freq.append(s.count(k))

# Bubble Sort
n = len(lst)
for i in range(n):
    for j in range(n-1):
        if freq[j] > freq[j+1]:
            freq[j], freq[j+1] = freq[j+1], freq[j]
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
