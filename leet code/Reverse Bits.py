# Reverse bits of a given 32 bits signed integer.

 

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
def reverseBits( n: int):
    s=bin(n)
    s=s[::-1]
    s=s[:-2]
    s=s+((32-len(s))*'0')# here I complete the lingth of num to 32 bit by adding the required zeroes
    return int(s,2)
print(reverseBits(43261596))
# 964176192