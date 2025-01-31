import pandas as pd
from sql_connection import engine

engine.connect()
 
query = """
select EQPID, DESCRIPTION, LOCATIONID, STATUS, EQPTYPE, ISPARENT, ISCHILD, PARENTEQPID, BATCHIDPREFIX
from plld.equn@sgodsprd
where LOCATIONID LIKE 'S%'
and EQPTYPE != 'HISTORY'
and STATUS in ('AVAIL','NOWIP')
"""

df = pd.read_sql(query, con=engine)
df_parent = df[df['parenteqpid'] == ' ']
df_child = df[df['parenteqpid'] != ' ']                         # rows where eqpid has a parent
parent_id = df_child['parenteqpid'].unique()

df_filtered = df_parent[~df_parent['eqpid'].isin(parent_id)]    # rows where eqpid is not a parent
df_dropped = df_parent[df_parent['eqpid'].isin(parent_id)]      # rows where eqpid is a parent 

df_combined = pd.concat([df_child, df_filtered], ignore_index=True)
print(df_combined)

# df_combined: EQPID, DESCRIPTION, LOCATIONID, STATUS, EQPTYPE, ISPARENT, ISCHILD, PARENTEQPID, BATCHIDPREFIX
df_combined.to_csv('equn_chamber.csv', index=False)