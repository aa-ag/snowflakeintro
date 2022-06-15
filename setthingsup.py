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

conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")

