from Errors import LowBalanceError
from Transaction import Transaction
from db_conn import my_cursor, conn

class Account:
    count = 0
    def __init__(self, acct_ID: int=None, balance: float=None, acct_type: str=None, cust_ID: int=None) -> None:
        self.acct_ID = acct_ID
        self.balance = balance
        self.acct_type = acct_type
        self.cust_ID = cust_ID

        self.insert_account()
    
    def insert_account(self) -> None:
        insert_sql = 'INSERT INTO account(acct_ID,balance,acct_type,cust_ID) \
            VALUES(%s,%s,%s,%s)'
        val = (self.acct_ID, self.balance, self.acct_type, self.cust_ID)
        
        my_cursor.execute(insert_sql, val)
        conn.commit()
    

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
    

    @staticmethod
    def get_all_accounts_by_cust_ID(c_ID: int):
        sql = f'SELECT * FROM account WHERE cust_ID = {c_ID}'
        my_cursor.execute(sql)
        Account.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result
    

    @staticmethod
    def get_account_balance_by_acct_ID(a_ID: int) -> float:
        sql = f'SELECT balance FROM account WHERE acct_ID = {a_ID}'
        my_cursor.execute(sql)
        bal = my_cursor.fetchone()[0]
        return bal


    @staticmethod
    def update_balace(acct_ID: int, new_balance: float) -> str:
        
        sql = f'UPDATE account SET balance = {new_balance} \
            WHERE acct_ID = {acct_ID}'
        
        my_cursor.execute(sql)
        conn.commit()


    