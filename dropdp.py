import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()
for i in range(len(drop_table_queries)) :
    cur.execute(drop_table_queries[i])
    conn.commit()