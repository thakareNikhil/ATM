from Exceptions import *
x=72000
def PIN(n):
    a=409409
    if n!=a:
        raise InvalidPin
    else:
        print(f'Your Current Balance is ₹{x}')

def DEP(n,m):
    global x
    a=123296
    if n!=a:
        raise InvalidAc
    else:
        print('-'*50)
        print('<=Account Found=>')
        print('-' * 50)
        print('AC Holder Name:Ravi Shankar')
        if m<=0:
            raise NegativeAmount
        else:
            print('Deposit Successful.... ')
            x=m+x

def WDW(n,m):
    global x
    a=409409
    if n!=a:
        raise InvalidPin
    elif x==0:
        raise ZeroAmount
    elif m>x:
        raise InsufficientBalance
    else:
        print('-' * 50)
        print('AC Holder Name:Ravi Shankar')
        if m<=0:
            raise NegativeAmount
        else:
            print('Withdraw Successful.... ')
            x=x-m
