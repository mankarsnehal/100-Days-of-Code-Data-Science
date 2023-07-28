from datetime import datetime
from Account import Account
from Errors import LowBalanceError
from Transaction import Transaction
from Transfer import Transfer



def deposit_amt(id,today):
    amount = float(input('Enter amount to deposit: '))
    type = 'Deposit'
    existing_bal = Account.get_account_balance_by_acct_ID(id)
    new_balance = existing_bal + amount
    Account.update_balace(id, new_balance)

    trans = Transaction(0,id,type,amount,today)
    print(amount,'Deposited Successfully..\n')


def withdraw_amt(id, today):
    amount = float(input('Enter amount to withdraw: '))
    type = 'Withdraw'
    existing_bal = Account.get_account_balance_by_acct_ID(id)

    try:   
        if existing_bal<amount:
            raise LowBalanceError
        elif existing_bal>=amount:
            new_balance = existing_bal - amount
            Account.update_balace(id, new_balance)
    except LowBalanceError:
        print('Cannot perform withdraw operation..')
        print('Check Account balance first..')
        return

    trans = Transaction(0,id,type,amount,today)
    print(amount,'Withdrawal Successful..\n')


def tranfer_amt(f_ID, today):
    t_ID = int(input('Enter account id: '))
    amount = float(input('Enter amount to tranfer: '))
    existing_bal = Account.get_account_balance_by_acct_ID(f_ID)
    try:   
        if existing_bal<amount:
            raise LowBalanceError
        elif existing_bal>=amount:
            f_bal = existing_bal - amount
            t_bal = existing_bal + amount
            Account.update_balace(f_ID, f_bal)
            Account.update_balace(t_ID, t_bal)
    except LowBalanceError:
        print('Cannot perform Transfer operation..')
        print('Check Account balance first..')
        return
        
    transfer = Transfer(0,f_ID,t_ID,amount,today)
    print(amount,'Transfer Successful..\n')


def list_trans(id: int):
    trans_list = Transaction.get_all_transactions_by_acct_ID(id)
    if len(trans_list) == 0:
        print('\nNo transactions performed yet..')
    else:
        print(f'\nAll the Transactions on the account ID({id}) are: ')
        for trans in trans_list:
            print('Transaction Type: ',trans[2],end='\t')
            print('Transaction Amount: ',trans[3],end='\t')
            print('Transaction Time: ',trans[4])
        





def acct_menu(id):
    while True:
        print('\n|****** Perform following Account Operations ******|')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Tranfer')
        print('4. List all Transactions')
        print('5. Check Account Balance')
        print('6. Exit')
        ch = int(input('Enter your choice: '))
        now = datetime.now()
        today = now.strftime("%Y-%m-%d %H:%M:%S")
        
        match ch:
            case 1:
                print('\nWelcome to perform Deposit Operation...')
                deposit_amt(id, today)

            case 2:
                print('\nWelcome to perform Withdraw Operation...')
                withdraw_amt(id, today)

            case 3:
                print('\nWelcome to perform Transfer Operation...')
                tranfer_amt(id, today)

            case 4:
                list_trans(id)
                print()

            case 5:
                balance = Account.get_account_balance_by_acct_ID(id)
                print('\nBalance present in your account:')
                print(balance, '\n')

            case 6:
                print('\nThank you for performing operations..\n')
                return

            case _:
                print('\nChoose correct option...\n')
