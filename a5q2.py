s = input("Enter a string: ")

digits = []

for ch in s:
    if ch.isdigit():        # checks if ch is 0-9
        digits.append(int(ch))

if len(digits) == 0:
    print("No digits found in the string.")
else:
    total = sum(digits)
    avg = total / len(digits)
    print("Sum:", total)
    print("Average:", avg)
    print("Maximum:", max(digits))
    print("Minimum:", min(digits))
