import os
import snowflake.connector as snc

user=os.environ["USER"]
password=os.environ["SNOWPASSWORD"]
account=os.environ["ACCOUNT"]

ctx = snc.connect(
    user=user,
    password=password,
    account=account
)
cs = ctx.cursor()

try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()