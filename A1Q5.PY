# Input a five-digit number
num = int(input("Enter a five-digit number: "))

# Extract each digit
d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10

# Add 1 to each digit and take modulo 10 (to handle 9+1 -> 0)
d1 = (d1 + 1) % 10
d2 = (d2 + 1) % 10
d3 = (d3 + 1) % 10
d4 = (d4 + 1) % 10
d5 = (d5 + 1) % 10

# Combine digits to form the new number
new_num = d1*10000 + d2*1000 + d3*100 + d4*10 + d5

# Display the result
print("The new number is:", new_num)
