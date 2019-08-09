def rev_words(mys):
    myl = mys.split()
    myl = myl[::-1]
    revd = ' '.join(myl)
    return revd

assert rev_words('the sky is blue') == 'blue is sky the'
assert rev_words('') == ''
