def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    return [numer3 // gcd(numer3, denom3), denom3 // gcd(numer3, denom3)]

def gcd(number1, number2):
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)