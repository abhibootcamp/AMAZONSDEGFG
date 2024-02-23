#You are given an integer N. You need to convert all zeroes of N to 5.
def convertFive(n):
    res = 0
    rate = 1
    while n >0:
        rem = n%10
        if rem == 0:
            rem = 5
        res = rate * rem + res
        rate *= 10
        n //= 10
    return res
'''N = 1004
Output: 1554'''
