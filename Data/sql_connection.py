import sqlalchemy as sql
 
username = "FPSINPUT"
password = "SkyOra#DwhSch#2021"
host = "SGDWHDEV.ad.skynet"
port = "1521"
sid = "SGDWHDEV"
engine = sql.create_engine(f"oracle+oracledb://{username}:{password}@{host}:{port}/{sid}")
