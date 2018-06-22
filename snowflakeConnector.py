import snowflake.connector
import sys
import time
import xlrd
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

#using snowflake connector
def connect_snowflake():
  try:
    start = time.time()
    ctx = snowflake.connector.connect(
      user = "snowflake_user",
      password = "password",
      account = "snowflake_account",
      database = "snowflake_database",
      warehouse = "warehouse",
      schema = "schema_name",
    )
    return ctx
  except Exception as e:
    print("[SNOWFLAKE ERROR] - Unable to connect to snowflake")
    print(e)
    sys.exit(1)
    
ctx = connect_snowflake()
cs = ctx.cursor()
count = cs.execute("select count(*) from table_name")
cs.execute("commit")
cs.close()
ctx.close()

#another method using sqlalchemy
engine = create_engine(URL(
  account = "snowflake_account",
  user = "snowflake_user",
  password = "password",
  database = "snowflake_database",
  schema = "schema_name",
  warehouse = "warehouse",
))

try:
  connection = engine.connect()
  df = pd.read_excel(filename, sheet_name="Sheet1")
  #chose select columns in DF and also rearrange
  df1 = df.iloc[:,[1,5,4,8,9]]
  #mass insert entire dataframe to snowflake table. if table already exists, ensure column names match with headers in DF
  df1.to_sql(name='TABLE_NAME', con=connection, schema='schema_name', if_exists='append', index=False)
finally:
  connection.close()
  engine.dispose()
