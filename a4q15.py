strings = ["apple", "banana", "mango"]
key = input("Enter character: ")

for st in strings:
    print(st, "->", st.count(key))
