import queue
from datetime import timedelta
import pandas as pd

class Lot:
    def __init__(self, id, part_num, deadline, curr_time):
        self.id = id                                                # String
        self.part_id = part_num.getId()                             # String
        self.sequenced_flow = queue.Queue(part_num.getFlow())       # Queue<Recipe>
        self.tct = part_num.getTCT()                                # total cycle time
        self.state = 'NOWIP'                                        # set default state
        self.ACR = 1                                                # initializing ACR
        self.curr_time = curr_time                                  # int/long in seconds
        self.curr_recipe_time = 0                                   # to be updated when its processing in a machine
        self.deadline = timedelta(days=deadline).total_seconds()    # int/long in seconds
        self.machineid_list = []                                    # for generating output
        self.recipe_list = []                                       # for generating output
        self.time_in_list = []                                      # for generating output
        self.time_out_list = []                                     # for generating output
    
    def updateLot(self, state, curr_time, curr_recipe_time, machineid, recipe, time_in, time_out):
        self.state = state
        self.curr_time = curr_time
        self.curr_recipe_time = curr_recipe_time
        self.machineid_list.append(machineid)
        self.recipe_list.append(recipe)
        self.time_in_list.append(time_in)
        self.time_out_list.append(time_out)
    
    def calculateACR(self):                                         # call this function at time_out
        return self.getRemainingTimeInSeconds() / self.getTheoreticaRemainingTime()
    
    def updateACR(self):
        self.ACR = self.calculateACR()

    def getNextRecipe(self):
        return self.sequenced_flow.get()
    
    def getRemainingTime(self):
        return self.deadline - self.curr_time
    
    def getTheoreticalRemainingTime(self):
        return self.tct - self.curr_time

    def getState(self):
        return self.state
        
    def getFutureEventList(self):
        df = pd.DataFrame({
            'MachineID': self.machineid_list,
            'Recipe': self.recipe_list,
            'Time_In': self.time_in,
            'Time_Out': self.time_out
        })
        return df