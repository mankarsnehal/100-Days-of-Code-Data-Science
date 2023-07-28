from Account import Account
from Customer import Customer
from New_Menu import display_menu
from Transaction import Transaction
import re

from create_customer import create_cust
from cust_login import login



if __name__ == '__main__':


    while True:
        print('|************** Welcome to Py_Bank ***********|')
        print('1. Login')
        print('2. Create Customer')
        print('3. Exit')
        ch = int(input('Enter your choice: '))
        print()
        match ch:
            case 1:
                print('Enter your credentials..')
                user_dict = login()
                # print(user_dict)
                display_menu(user_dict)
                

            
            case 2:
                print('|*********** Sign Up to the Py_Bank ****************|')

                user_dict = create_cust()

                cust = Customer(0, user_dict['f_name'], user_dict['m_name'], user_dict['l_name'], 
                                user_dict['username'], user_dict['password'], user_dict['address'], 
                                user_dict['birth_date'], user_dict['phone'], user_dict['email'], 
                                user_dict['age'])
                
                print('Congratulations for Signing Up Successfully..\n\n')

            case 3:
                print('Thank You for visiting the Py_Bank...')
                break

            case _:
                print('Please choose correct choice again...\n')

    # acct = Account()
    # tran = Transaction()


