from Account import Account


def create_acct(user_dict):
    while True:
        print('1. Current Account.')
        print('2. Savings Account.')
        print('3. Fixed Account.')
        ch = int(input('Enter your choice: '))

        match ch:
            case 1:
                type = 'Current'
            case 2:
                type = 'Savings'
            case 3:
                type = 'Fixed'
            case _:
                print('Choose correct option from the menu...')
        
        amount = float(input('Enter amount you want to deposit: '))

        acct = Account(0, amount, type, user_dict['cust_ID'])
        break

    print('End..')