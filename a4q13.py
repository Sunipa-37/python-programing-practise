s = input("Enter string: ")

unique_chars = []
for ch in s:
    if ch not in unique_chars:
        unique_chars.append(ch)

max_char = ''
max_freq = 0

for ch in unique_chars:
    count = s.count(ch)
    if count > max_freq:
        max_freq = count
        max_char = ch

print("Maximum frequency character:", max_char, "=", max_freq)
