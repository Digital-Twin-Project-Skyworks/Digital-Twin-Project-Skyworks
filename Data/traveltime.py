import pandas as pd
import sqlalchemy as sql
import numpy as np

# db connection
# username = "FPSINPUT"
# password = "SkyOra#DwhSch#2021"
# host = "SGDWHDEV.ad.skynet"
# port = "1521"
# sid = "SGDWHDEV"

# engine = sql.create_engine(f"oracle+oracledb://{username}:{password}@{host}:{port}/{sid}")
from sql_connection import engine
engine.connect()

# Define SQL query
query = """
WITH FilteredData AS (
    SELECT
        LOTID,
        LOCATION,
        QUEUETIME,
        TRACKOUTTIME
    FROM
        plld.hist@sgodsprd
    WHERE
        PRODAREA IN ('SINGAPORE', 'SINGAPORE3')
        AND QUEUETIME IS NOT NULL
        AND TRACKOUTTIME IS NOT NULL
        AND LOCATION IN ('SPACK', 'S3PACK', 'SGRIND', 'STEST', 'SPHOTO',
                         'SUB_PHOTO', 'S3TEST', 'S3ETCH', 'S3SPUT', 'S3SOLDER',
                         'S3PLTCHM', 'S3BOND', 'S3PHOTO', 'S3GRIND', 'SDICING',
                         'S3DICINGS', 'SOLDER', 'S3PLATE', 'SPLATES', 'SPUTTER',
                         'S3DRYETCH')
        AND TIMESTAMPTIME >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
        AND TIMESTAMPTIME < TO_DATE('2025-01-01', 'YYYY-MM-DD')
),
TravelTimes AS (
    SELECT
        A.LOTID,
        A.LOCATION AS LOCATION_A,
        B.LOCATION AS LOCATION_B,
        CAST((B.QUEUETIME - A.TRACKOUTTIME) * 24 * 60 * 60 AS INT) AS TRAVEL_TIME_SECONDS
    FROM
        FilteredData A
    JOIN
        FilteredData B
        ON A.LOTID = B.LOTID
        AND A.LOCATION <> B.LOCATION
        AND B.QUEUETIME > A.TRACKOUTTIME
    WHERE (B.QUEUETIME - A.TRACKOUTTIME) * 24 * 60 * 60 < 7200
)
SELECT 
    LOCATION_A,
    LOCATION_B,
    COUNT(*) AS count,
    AVG(TRAVEL_TIME_SECONDS) AS mean,
    MIN(TRAVEL_TIME_SECONDS) AS lower_bound,
    MAX(TRAVEL_TIME_SECONDS) AS upper_bound
FROM TravelTimes
GROUP BY LOCATION_A, LOCATION_B
"""

# Fetch data into Pandas DataFrame
df = pd.read_sql(query, con=engine)

# Save as CSV file
csv_filename = "traveltime_all_version.csv"
df.to_csv(csv_filename, index=False)

print(f"Data has been saved to {csv_filename}")