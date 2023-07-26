from db_conn import my_cursor, conn

class Account:
    count = 0
    def __init__(self, acct_ID: int=None, balance: float=None, acct_type: str=None, cust_ID: int=None) -> None:
        self.acct_ID = acct_ID
        self.balance = balance
        self.acct_type = acct_type
        self.cust_ID = cust_ID

        insert_sql = 'INSERT INTO account(acct_ID,balance,acct_type,cust_ID) \
            VALUES(%s,%s,%s,%s)'
        # val = (acct_ID, balance, acct_type, cust_ID)
        val = (1,50000,'Savings',1)
        
        my_cursor.execute(insert_sql, val)
        conn.commit()
        print(my_cursor.rowcount, ' Account created..')
    

    def __get_all_accounts(self) -> list:
        sql = 'SELECT * FROM account'
        my_cursor.execute(sql)
        Account.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result
    

    @classmethod
    def _get_accounts_count() -> int:
        sql = 'SELECT COUNT(*) FROM account'
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        Account.count = result
        return result
    

    @classmethod
    def get_all_accounts_by_cust_ID(c_ID: int) -> Account:
        sql = f'SELECT * FROM account WHERE cust_ID = {c_ID}'
        my_cursor.execute(sql)
        Account.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result
    

    @classmethod
    def get_all_accounts_count_by_cust_ID(c_ID: int) -> int:
        sql = f'SELECT COUNT(*) FROM account WHERE cust_ID = {c_ID}'
        my_cursor.execute(sql)

        result = int(my_cursor)
        return result
    