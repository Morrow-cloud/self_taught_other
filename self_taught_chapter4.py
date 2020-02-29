# 1.
def square(x):
    '''
    Squares x.
    :param num: int
    :return: int square of x
    '''
    return num ** 2

# 2.
def print_string(s):
    '''
    Print s.
    :param: s : string
    '''
    print(s)

# 3.
def some_arguments(a, b, c, d=False, e=None):
    '''
    Takes three positional arguments and two keyword arguments.
    '''
    pass

# 4.
def div_half(n):
    '''
    Divide argument by 2.
    :param: n: int
    :return : n / 2
    '''
    return int(n / 2)

def four_times(m):
    '''
    Multiply the argument by 4.
    :param: m: int
    :return: m * 4
    '''
    return m * 4

n = div_half(4)
four_times(n)

# 5.
def float_string(e):
    '''
    For testing, Convert string to decimal.
    :param: e: string
    '''
    try:
        return float(string)
    except ValueError:
        print('文字列は少数に変換できません')

