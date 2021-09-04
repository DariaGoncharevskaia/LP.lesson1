def get_summ(one, two, delimiter = '&'):
    one = str(one).upper()
    two = str(two).upper()
    st = one + ' ' + delimiter + ' ' + two
    return st
    

print(get_summ('Learn', 'python'))

