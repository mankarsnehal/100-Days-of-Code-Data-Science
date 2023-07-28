from Account import Account
from Account_menu import acct_menu
from create_account import create_acct


def list_accts(user_dict):
    acct_list = Account.get_all_accounts_by_cust_ID(user_dict['cust_ID'])
    if len(acct_list)==0:
        print('\nYou have no Accounts...\n')
    else:
        print('\nYour all Accounts are: ')
        for acct in acct_list:
            print("Account ID: ",acct[0],end='\t')
            print("Account Type: ",acct[2],end='\t')
            print("Account Balance: ",acct[1])
        print()


def display_menu(user_dict):
    while True:
        print(f'\n|************* Welcome to the Bank, { user_dict["f_name"] } ***************|')
        print('1. Create new Account')
        print('2. Choose Existing Account')
        print('3. List all the Existing Account')
        print('4. Logout from the Bank System')
        ch = int(input('\nEnter your choice: '))

        match ch:
            case 1:
                print('Create new Account...')
                create_acct(user_dict)
                break

            case 2:
                a_ID = int(input('Enter your Account ID: '))
                acct_menu(a_ID)

            case 3:
                list_accts(user_dict)

            case 4:
                print('\nLogout Successful..\n')
                return
            
            case _:
                print('Choose correct option...')
    
    print('End...')