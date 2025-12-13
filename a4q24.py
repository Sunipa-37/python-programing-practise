# Input string
s = input("Enter a string: ")

# Replace commas with a temporary character (say, #)
s = s.replace(',', '#')
# Replace dots with commas
s = s.replace('.', ',')
# Replace temporary character with dots
s = s.replace('#', '.')

print("Modified string:", s)
