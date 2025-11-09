##Problem statement:Input a sequence of 8 integers, count how many blocks of consecutive increasing numbers exist. A block is defined as one or more numbers such that each number after the first in the block is strictly greater than its predecessor. For example [2, 3, 5, 1, 2, 3, 3, 4] has: first block [2,3,5], then second block [1,2,3], skip the 3 to 3 since not strictly greater, then third block [3,4]. So the answer would be 3. Also print the length of the longest block.
#Input: A list of integers (length ≥ 1).
#Output: Two integers: number of increasing-blocks, and length of the longest block.




n = list(map(int, input("Enter 8 integers: ").split()))

cb= 0
ml = 1
cl = 1

for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        cl += 1
    else:
        cb += 1
        ml = max(ml, cl)
        cl = 1

# Count the last block
cb += 1
ml = max(ml, cl)

print(cb, ml)
