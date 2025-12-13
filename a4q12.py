s = input("Enter string: ")

least_char = s[0]
least_count = len(s)

for ch in s:
    # count frequency manually
    current_count = 0
    for x in s:
        if x == ch:
            current_count += 1
    
    # update least frequent
    if current_count < least_count:
        least_count = current_count
        least_char = ch

print("Least Frequent Character:", least_char)
print("Frequency:", least_count)
