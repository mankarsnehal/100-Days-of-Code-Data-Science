from Customer import Customer


def login():
    while True:
        username = input('Enter username: ')
        user = Customer.get_cust_by_username(username)
        print(user)
        if type(user) == tuple:
            password = input('Enter password: ')
            print(user[5], password)
            if user[5] == password:
                print('Login Successful...')
                break
            else:
                print('Password Incorrect...')  
        else:
            print('Username Invalid...')
    
    key_list = ['cust_ID', 'f_name', 'm_name', 'l_name', 'username', 'password', 
                'address', 'birth_date', 'phone', 'email', 'age']
    user_dict = dict(zip(key_list, user))
    return user_dict
