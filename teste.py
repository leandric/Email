import os
import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', db = 'BASE_CLI')
print(conexao)

query = 'select * from base'

df = pd.read_sql_query(sql = query,con=conexao,index_col=None)
print(df.head())