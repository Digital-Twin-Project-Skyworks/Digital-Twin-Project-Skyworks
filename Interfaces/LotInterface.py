from collections import deque
from datetime import datetime, timedelta
import pandas as pd

class LotInterface:
    def __init__(self, id, part_num, start_time, deadline):
        self.id = id                                            # String
        self.part_id = part_num.id                              # String
        self.sequenced_flow = deque(part_num.sequenced_flow)    # deque<Recipe>
        self.start_time = start_time                            # datetime
        self.deadline = start_time + timedelta(days=deadline)   # int
        self.machineid_list = []                                # for generating output
        self.recipe_list = []                                   # for generating output
        self.time_in = []                                       # for generating output
        self.time_out = []                                      # for generating output

    def getRemainingTimeInSeconds(self):
        return (self.deadline - datetime.now()).total_seconds()
    
    def calculateACR(self, TCT):
        return self.getRemainingTimeInSeconds() / TCT
    
    def getFutureEventList(self):
        df = pd.DataFrame({
            'MachineID': self.machineid_list,
            'Recipe': self.recipe_list,
            'Time_In': self.time_in,
            'Time_Out': self.time_out
        })
        return df