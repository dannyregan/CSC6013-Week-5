# Takes a real number, n, and returns the sum of all numbers squared from 1 to n.
def sumOfSquares(n):
    if n == 1:
        return n
    else:
        return n**2 + sumOfSquares(n-1)
    
# ======================================
print(sumOfSquares(12))
print(sumOfSquares(20))