import pandas as pd
from sql_connection import engine

engine.connect()
 
query = """
select t1.RECPNAME, t1.EQPTYPE, t2.EQPID
from plld.recp@sgodsprd t1
LEFT JOIN plld.equn@sgodsprd t2
ON t1.EQPTYPE = t2.EQPTYPE
"""

df = pd.read_sql(query, con=engine)

from equn_chamber import df_combined
eqpid = df_combined['eqpid'].unique()
df1 = df[df['eqpid'].isin(eqpid)].dropna()
print(df1)

# df1: recpname, eqptype, eqpid