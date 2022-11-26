strings: list = ['a', 'b', 'c', 'd']
# this is a 64-bit system, 4 * 8 = 32 bytes of storage

# Array/ List methods
strings.extend(['e', 'f', 'g', 'h'])  # appends each of these to the list, I think in O(n) time
a_index = strings.index('a')  # this happens before the insertion
a_count = strings.count('a')  # count how many times 'a' appeared
strings.insert(0, '*')  # insert * at index 0, takes O(n) time

# O(1) operations
strings.pop()
strings.append('i')

print(strings)
print(a_index)
print(a_count)
