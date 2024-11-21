# Takes a natural number, n, and returns the number of digits required to store that number in binary.
def binaryExpansion(n):
    if n == 1:
        return n
    else:
        return 1 + binaryExpansion(n//2)
    
# ======================================
print(binaryExpansion(256))
print(binaryExpansion(750))