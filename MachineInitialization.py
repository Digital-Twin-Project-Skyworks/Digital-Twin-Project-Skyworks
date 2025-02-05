import csv; import pandas as pd
from ClassesJustForHoldingData import Recipe
from Interfaces import MachineInterface
machines = {}
locs = {}

recptime = pd.read_csv("equn_recp.csv", usecols = ["recpname", "eqpid"])
eqchamber = pd.read_csv("equn_chamber.csv")
def parent(df1):
    counter = 0
    df = pd.DataFrame(columns = ["eqpid", "locationid"])
    dta = {}
    for index, row in df1.iterrows():
        
        if row["ischild"] == -1:
            #df = df.append({"eqpid" : row["parenteqpid"], "locationid": row["locationid"]}, ignore_index = True)
            dta[row["parenteqpid"]] = row["locationid"]
        else:
            #df = df.append({"eqpid" : row["eqpid"], "locationid" : row["locationid"]}, ignore_index = True)
            dta[row["eqpid"]] = row["locationid"]
    return dta
temp = parent(eqchamber)
def merge(dict1, df2):
    df2["locationid"] = df2["eqpid"].map(dict1)
    return df2

data1 = merge(temp, recptime) #This is the data needed for each machine

for index, row in data1.iterrows():
    if row["eqpid"] in machines:
        machines[row["eqpid"]].append(row["recpname"])
        
    else:
        machines[row["eqpid"]] = [row["recpname"]]
        locs[row["eqpid"]] = row["locationid"]

    
