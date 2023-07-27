from Account import Account
from create_account import create_acct


def display_menu(user_dict):
    print(f'|************* Welcome to the Bank, { user_dict["f_name"] } ***************|')
    print('1. Create new Account')
    print('2. Choose Existing Account')
    print('3. List all the Existing Account')
    print('4. Logout from the Bank System')
    while True:
        ch = int(input('\nEnter your choice: '))

        match ch:
            case 1:
                print('Create new Account...')
                create_acct(user_dict)
                break
            case 2:
                a_ID = int(input('Enter your Account ID: '))
                print('Perform following Account Operations..')
                

            case 3:
                print('Your all Accounts are: ')
                acct_list = Account.get_all_accounts_by_cust_ID(user_dict['cust_ID'])
                for acct in acct_list:
                    print(acct)
            case 4:
                print('Logout Successful..')
            case _:
                print('Choose correct option...')
    
    print('End...')