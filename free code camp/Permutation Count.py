from itertools import permutations
def count_permutations(s):
    chars=list(ch for ch in s)
    print(chars)
    return len(set(permutations(chars)))
print(count_permutations("freecodecamp"))