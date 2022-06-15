from settings import *
import snowflake.connector as snc

ctx = snc.connect(
    user=username,
    password=thisisnotapassword,
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