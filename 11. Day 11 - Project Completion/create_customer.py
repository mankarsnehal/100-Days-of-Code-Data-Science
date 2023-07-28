import re
from Customer import Customer

def username_input() -> str:
    while True:
        username = input('\nEnter username for you: ')
        user = Customer.get_cust_by_username(username)
        if type(user) == tuple:
            print('Username already exist..\nChoose another name for you..')
        else:
            break
    return username


def password_input() -> str:
    while True:
        print('Password should contain: \n1. Atleast 6 alphabetic character\
                \n2. Atleast 2 numeric Characters \
                \n3. Atleast 1 Capital alphabetic character \
                \n3. No Space Character')
        password = input('Enter password: ')
        char_count = re.findall('[A-Za-z]', password)
        int_count = re.findall('[\d]', password)
        sp_count = re.findall('[\s]', password)
        cap_count = re.findall('[A-Z]', password)

        if (len(char_count)>=6 and len(int_count)>=2 and len(cap_count)>=1 
            and len(sp_count)==0):
            print('Strong Password...')
            break
        else:
            print('Invalid Password..')
        
    return password


def birth_input() -> str:
    while True:
        email_pattern = re.compile('[\d]{4}-[\d]{2}-[\d]{2}')
        birth_date = input('Enter your birth date(YYYY-MM-DD): ')
        flag = email_pattern.search(birth_date)
        if flag:
            break
        else:
            print('Date not valid..')
    return birth_date


def phone_input() -> str:
    while True:
        phone = input('Enter your phone number(10 digit): ')
        pattern = re.compile('[\d]{10}')
        if pattern.search(phone):
            break
        else:
            print('Not Valid...')
    return phone


def email_input() -> str:
    while True:
        email_pattern = re.compile('[\w]+@[\w].[\w]+')
        email = input('Enter your email: ')
        flag = email_pattern.search(email)
        if flag:
            break
        else:
            print('Email not valid..')
    return email


def age_input() -> int:
    while True:
        try:
            age = int(input('Enter your age: '))
            break
        except:
            print('\nEnter age in integer: ')
    return age






def create_cust() -> dict:
    key_list = ['f_name', 'm_name', 'l_name', 'username', 'password', 'address', 
                            'birth_date', 'phone', 'email', 'age']
    user_dict = dict.fromkeys(key_list)
    
    # Full name Input
    full = input('Enter full name(first middle last):')
    user_dict['f_name'], user_dict['m_name'], user_dict['l_name'] = full.split(' ')

    # username Input
    user_dict['username'] = username_input()
    
    # Password Input
    print()
    user_dict['password'] = password_input()

    # Address Input
    print()
    user_dict['address'] = input('Enter your address: ')

    # Birth Date Input
    print()
    user_dict['birth_date'] = birth_input()

    # Phone Number Input
    print()
    user_dict['phone'] = phone_input()

    # Email Input
    print()
    user_dict['email'] = email_input()

    # Age Input
    print()
    user_dict['age'] = age_input()
    print()



    return user_dict