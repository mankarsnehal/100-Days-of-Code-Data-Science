from db_conn import my_cursor, conn

class Customer:
    count = 1
    def __init__(self, cust_ID: int, f_name: str, m_name: str, l_name: str, username: str, password: str, address: str, birth_date: str, phone: int, email: str, age: int) -> None:
        self.cust_ID = cust_ID
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.username = username
        self.__password = password
        self.address = address
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.age = age



    def insert_cust(self) -> str:
        insert_sql = 'INSERT INTO customer(cust_ID, f_name, m_name, l_name, username, password, \
            address, birth_date, phone, email, age) \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        val = (Customer.count, self.f_name, self.m_name, self.l_name, 
               self.username, self.password, self.address, self.birth_date, 
               self.phone, self.email, self.age)
        
        my_cursor.execute(insert_sql, val)
        conn.commit()
        return my_cursor.rowcount+' Customer created..'
    

    def update_password(self, password: str) -> None:
        self.__password = password
        update_sql = 'UPDATE customer SET password = %s, where cust_ID = %s'
        val = (password, self.cust_ID)
        my_cursor.execute(update_sql, val)
    

    def __str__(self) -> str:
        return f'''
        
        '''
    

    @classmethod
    def _get_cust_count() -> int:
        sql = 'SELECT COUNT(*) FROM customer'
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        Customer.count = result
        return result
    

    def __get_all_cust(self) -> list :
        sql = 'SELECT * FROM customer'
        my_cursor.execute(sql)
        Customer.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result


    @classmethod
    def get_cust_by_id(id: int) -> Customer:
        sql = f'SELECT * FROM customer WHERE id = {id}'
        my_cursor.execute(sql)
        result = my_cursor.fetchone()
        return result
    

    @classmethod
    def get_cust_by_username(u_name: str) -> Customer:
        sql = f'SELECT * FROM customer WHERE username = {u_name}'
        my_cursor.execute(sql)
        result = my_cursor.fetchone()
        return result


