import csv, json; import pandas as pd
from ClassesJustForHoldingData.Recipe import Recipe
from ClassesWithMethodsToBeDefined.Lot import Lot
from ClassesWithMethodsToBeDefined.Machine import Machine


# Recipe Initialisation
recipes = {}
recptimes = pd.read_csv("Data/recptime_active_version.csv")
for index, row in recptimes.iterrows():
    id = row["recpname"]
    recp = Recipe(id, int(row["active_lower_bound"]),  int(row["active_upper_bound"]))
    recipes[id] = recp

# Machine Initialisation
machines = {}
locs = {}

recptime = pd.read_csv("Data/equn_recp.csv", usecols = ["recpname", "eqpid"])
eqchamber = pd.read_csv("Data/equn_chamber.csv")
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
all_machines = {}
for index, row in data1.iterrows():
    if row["recpname"] in recipes:
        if row["eqpid"] in machines:
            machines[row["eqpid"]].append(recipes[row["recpname"]])
        
        else:
            machines[row["eqpid"]] = [recipes[row["recpname"]]]
            locs[row["eqpid"]] = row["locationid"]
for key in machines:
    all_machines[key] = Machine(key, machines[key], locs[key])

# Machines is a dictionary with the key as machine id, and value of recipe list    
# Locs is a dictionary with the key as machine id and value of location id
# all_machines is the machine id with the list of machines

# Lot Initialisation
with open('Data/PartID_Recipe.json', 'r') as file:
    data = json.load(file)
counter = 1000000
for entry in data:
    part_num = entry['partname']
    Lot(counter, part_num, 1, 2) #time values tbc
    counter += 1