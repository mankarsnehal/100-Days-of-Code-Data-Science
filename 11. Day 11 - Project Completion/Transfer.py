from datetime import datetime
from db_conn import my_cursor, conn

class Transfer:

  def __init__(self, transfer_ID: int, from_acct_ID: int, to_acct_ID: int, amount: float, transfer_date: datetime) -> None:
    self.transfer_ID = transfer_ID
    self.from_acct_ID = from_acct_ID
    self.to_acct_ID = to_acct_ID
    self.amount = amount
    self.transfer_date = transfer_date

    self.insert_transfer()

  def insert_transfer(self) -> str:
    insert_sql = 'INSERT INTO transfers(transfer_ID,from_acct_ID,to_acct_ID,amount,transfer_date) \
        VALUES(%s,%s,%s,%s,%s)'
    val = (self.transfer_ID, self.from_acct_ID, self.to_acct_ID, self.amount, self.transfer_date)
    
    my_cursor.execute(insert_sql, val)
    conn.commit()
