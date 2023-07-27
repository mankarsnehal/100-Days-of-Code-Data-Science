from datetime import datetime
from decimal import Decimal
import re

from Customer import Customer
from New_Menu import display_menu
from create_account import create_acct
from cust_login import login

# user_dict = login()
# print(user_dict)

user_dict = {'cust_ID': 1, 'f_name': 'snehal', 'm_name': 'sanjay', 'l_name': 'mankar', 
             'username': 'snehalmankar', 'password': 'snehal21', 'address': 'kop', 
             'birth_date': 'datetime.date(2001, 8, 21)', 'phone': '9730990136', 
             'email': 'snehal@gmail.com', 'age': 22}

display_menu(user_dict)

# create_acct(user_dict)



print('End.....')
