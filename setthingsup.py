import os
import snowflake.connector as snc

user=os.environ["USER"]
password=os.environ["SNOWPASSWORD"]
account=os.environ["ACCOUNT"]

conn = snc.connect(
    user=user,
    password=password,
    account=account
)

# conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
# conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb")
conn.cursor().execute("USE DATABASE testdb")
# conn.cursor().execute(
#     "CREATE OR REPLACE TABLE "
#     "test_table(col1 integer, col2 string)")
# conn.cursor().execute(
#     "INSERT INTO test_table(col1, col2) "
#     "VALUES(123, 'test string1'),(456, 'test string2')")
col1, col2 = conn.cursor().execute("SELECT col1, col2 FROM test_table").fetchone()
print('{0}, {1}'.format(col1, col2))