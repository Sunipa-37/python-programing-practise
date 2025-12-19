

l= [2, 3, 5, 7, 6, 4, 1, 2, 1]

n = len(l)
list_len = 0
sub_seq = []

i = 1

while i < n - 1:
    if l[i] > l[i-1] and l[i] > l[i+1]:

        left = i - 1
        while left > 0 and l[left] > l[left-1]:
            left -= 1
        
        right = i + 1
        while right < n - 1 and l[right] > l[right+1]:
            right += 1
        
        length = right - left + 1

        if length > list_len: 
            list_len = length
            sub_seq = l[left:right+1]

        i = right

    else:
        i+=1

if list_len == 0:
    print('None')
else:
    print('Length: ', list_len)
    print('Subsequence: ',sub_seq)
