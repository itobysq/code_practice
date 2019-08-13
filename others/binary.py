def to_binary(num):
    """
    use recursion to convert a number to binary
    """
    return recurs(num, '')[::-1]

def recurs(num, binstr):
    if num == 0 or num == 1:
        return binstr + str(num)

    else:
        last_digit = str(num % 2)
        return recurs(num // 2, binstr + last_digit)

assert to_binary(5) == '101'
assert to_binary(4) == '100'
