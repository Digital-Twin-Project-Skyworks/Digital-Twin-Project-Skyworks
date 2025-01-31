import sqlalchemy as sql
import pandas as pd
 
username = "FPSINPUT"
password = "SkyOra#DwhSch#2021"
host = "SGDWHDEV.ad.skynet"
port = "1521"
sid = "SGDWHDEV"
engine = sql.create_engine(f"oracle+oracledb://{username}:{password}@{host}:{port}/{sid}")

engine.connect()
 
query = """
select t1.EQPID, t1.EQPTYPE, t2.RECPNAME
from plld.equn@sgodsprd t1
LEFT JOIN plld.recp@sgodsprd t2
ON t1.EQPTYPE = t2.EQPTYPE
"""

df = pd.read_sql(query, con=engine)

from equn_chamber import df_combined
eqpid = df_combined['eqpid'].unique()
df2 = df[df['eqpid'].isin(eqpid)].dropna()

from equn_recp import df1
df2_reordered = df2[df1.columns]

df1.reset_index(drop=True, inplace=True)
df2_reordered.reset_index(drop=True, inplace=True)

df1_sorted = df1.sort_values(by=list(df1.columns)).reset_index(drop=True)
df2_sorted = df2_reordered.sort_values(by=list(df2_reordered.columns)).reset_index(drop=True)

# Check if the DataFrames are identical
comparison_result = df1_sorted.equals(df2_sorted)
print("Are the DataFrames identical?:", comparison_result)