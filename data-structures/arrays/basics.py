''' Arrays '''

strings = ['a', 'b', 'c', 'e']

strings[2] # c - O(1)

strings.append('y') # a, b, c, d, e, y - O(n)

strings.pop() # a, b, c, d, e - O(n)

strings.pop(2) # a, b, e

strings.remove('a') # b, e

strings.insert(1, 'x') # b, x, e

x = len(strings) # 3 elements

'''
    Merge sorted arrays
    array1 = [0, 3, 4, 31]
    array2 = [4, 6, 30]
    result: [0, 3, 4, 5, 6, 30, 31]
'''
array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

#Easy way
merged = array1 + array2
merged.sort()
print(merged)