from Exceptions import InvalidPin,NegativeAmount,InvalidAc,ZeroAmount,InsufficientBalance #Those are prog-def exceptions
from function import PIN,DEP,WDW #Those are prog-def functions for raise the prog-def exceptions
while True:
    print('>'*50)
    print('Welcome to State Bank of India'.center(50))
    print('<'*50)
    print("""
    1.Check Balance
    2.Deposit
    3.Withdraw
    4.Exit""")
    print('='*50)
    a=input('Enter your choice:')
    print('-'*50)
    match a:
        case '1':
            a=1
            while a<=3:
                try:
                    b=int(input('Entre PIN:'))
                    PIN(b)
                    break
                except (ValueError,InvalidPin):
                    if a<3:
                        print('Invalid PIN Try again',a)
                    else:
                        print('Invalid PIN')
                a+=1
            else:
                print('-'*50)
                print('You Cross Your Pin Limit'.center(50))
        case '2':
            try:
                a=int(input('Entre Account No:'))
                b=int(input('Entre Amount:₹'))
                DEP(a,b)
            except (ValueError,NegativeAmount):
                print('Invalid Amount')
            except InvalidAc:
                print('Invalid AC No: Try again')

        case '3':
            l=1
            while l<=3:
                try:
                    a = int(input('Entre PIN No:'))
                    b = int(input('Entre Amount:₹'))
                    WDW(a,b)
                    break
                except (ValueError, NegativeAmount):
                    print('Invalid Amount')
                    break
                except InvalidPin:
                    if l<3:
                        print('Invalid PIN Try again',l)
                    else:
                        print('Invalid PIN')
                except ZeroAmount:
                    print('Your AC Balance is Zero')
                    break
                except InsufficientBalance:
                    print('Insufficient Balance')
                    break
                l+=1
        case '4':
            print('Thank you for Visit in State Bank of India'.center(50))
            print('x'*50)
            exit()
        case _:
            print('Invalid choice')
