import queue
from datetime import timedelta
import pandas as pd

class Lot:
    def __init__(self, id, part_num, deadline):
        self.id = id                                                # String
        self.part_id = part_num.getId()                             # String
        self.sequenced_flow = queue.Queue(part_num.getFlow())       # Queue<Recipe>
        self.tct = part_num.getTCT()                                # total cycle time
        self.state = 'NOWIP'                                        # set default state
        self.ACR = 1                                                # initializing ACR
        self.curr_recipe_time = 0                                   # to be updated when its processing in a machine
        self.deadline = timedelta(days=deadline).total_seconds()    # int/long in seconds
        self.fel = []                                               # for generating output
        self.location = ''                                          # String
    
    def updateLot(self, state, curr_recipe_time, machineid, recipe, time_in, time_out, location):
        self.state = state
        self.curr_recipe_time = curr_recipe_time
        self.fel.append([machineid, recipe, time_in, time_out])
        self.location = location
    
    def calculateACR(self):                                         # call this function at time_out
        return self.getRemainingTimeInSeconds() / self.getTheoreticaRemainingTime()
    
    def updateACR(self):
        self.ACR = self.calculateACR()

    def getNextRecipe(self):
        return self.sequenced_flow.get()
    
    def getRemainingTime(self, curr_time):
        return self.deadline - curr_time
    
    def getTheoreticalRemainingTime(self, curr_time):
        return self.tct - curr_time

    def getState(self):
        return self.state
        
    def getFutureEventList(self):
        column_names = ['MachineID', 'Recipe', 'Time_In, Time_Out']
        df = pd.DataFrame(self.fel, columns=column_names)
        return df