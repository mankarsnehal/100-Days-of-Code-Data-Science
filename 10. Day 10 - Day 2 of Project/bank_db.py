from db_conn import my_cursor, conn



cust_sql = 'CREATE TABLE customer(cust_ID INT PRIMARY KEY AUTO_INCREMENT, f_name VARCHAR(20), \
  m_name VARCHAR(20), l_name VARCHAR(20), username VARCHAR(20), password VARCHAR(50), \
    address VARCHAR(45), birth_date DATE, phone DECIMAL(10,0), email VARCHAR(45), age INT)'
my_cursor.execute(cust_sql)

acct_sql = 'CREATE TABLE account(acct_ID INT PRIMARY KEY AUTO_INCREMENT, balance FLOAT, \
  acct_type VARCHAR(20), cust_ID INT, \
    CONSTRAINT FK_cust_ID FOREIGN KEY (cust_ID) REFERENCES customer(cust_ID))'
my_cursor.execute(acct_sql)

tran_sql = 'CREATE TABLE transaction(trans_ID INT PRIMARY KEY AUTO_INCREMENT, \
  acct_ID INT, transac_date DATE, ammount FLOAT, transac_type VARCHAR(20), \
    CONSTRAINT FK_acct_ID FOREIGN KEY (acct_ID) REFERENCES account(acct_ID))'
my_cursor.execute(tran_sql)

