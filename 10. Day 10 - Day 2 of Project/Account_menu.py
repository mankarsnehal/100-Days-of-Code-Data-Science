

def acct_menu():
    while True:
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Exit')
        ch = int(input('Enter your choice: '))
        match ch:
            case 1:
                amount = float(input('Enter amount to deposit: '))
            case 2:
                amount = float(input('Enter amount to withdraw: '))
            case 3:
                return
            case _:
                print('Choose correct option...')
