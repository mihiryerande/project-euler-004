# Problem 004:
#     Largest Palindrome Product
#
# Description:
#     A palindromic number reads the same both ways.
#     The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#     Find the largest palindrome made from the product of two 3-digit numbers.

from math import ceil, floor


def is_palindrome(x):
    """
    Return True iff `x` is a 'palindrome' (i.e. a palindromic number),
      meaning its digits read the same both forwards and backwards.

    Args:
        x (int): Natural number

    Returns:
        True iff `x` is a palindrome
    """
    # Choosing not to use cheap trick with str
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits == digits[::-1]


def main(n):
    """
    Return a 3-tuple containing the largest palindrome made from the product of two `n`-digit numbers,
      as well as the two factors themselves.
    Note that this is specifically in decimal (base-10).

    Args:
        n (int): Natural number

    Returns:
        Returns factors and product as tuple, in order (x, y, x*y)

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # Iterate downwards from the highest possible product... but in a ~cool~ way!
    # Go through every potential pair of factors in the following way,
    #   choose the midpoint of the two factors,
    #   then step the factors away from the midpoint until one is out of bounds.

    # Bounds
    bnd_hi = 10 ** n - 1
    bnd_lo = 10 ** (n-1)

    # Start iterating midpoint from its highest possible value
    mid = bnd_hi
    while mid >= bnd_lo:
        lo = floor(mid)
        hi = ceil(mid)
        while bnd_lo <= lo and hi <= bnd_hi:
            prod = lo * hi
            if is_palindrome(prod):
                return lo, hi, prod
            else:
                lo -= 1
                hi += 1
        mid -= 0.5
    return None, None, None


if __name__ == '__main__':
    d = int(input('Enter a number of digits: '))
    p, q, r = main(d)
    print('Largest palindromic product of two {}-digit numbers:\n{} * {} = {}'.format(d, p, q, r))
