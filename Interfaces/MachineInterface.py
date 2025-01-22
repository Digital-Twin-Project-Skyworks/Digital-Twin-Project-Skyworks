from collections import deque
from datetime import datetime, timedelta
import pandas as pd

class MachineInterface:
    def __init__(self, recipes):
        self.id = id                                            # String
        self.serving = False                                    # boolean
        self.recipes = recipes                                  # List<Recipe>
        self.queue = deque()                                    # deque<Lot>
        self.lotid_list = []                                    # for generating output
        self.recipe_list = []                                   # for generating output
        self.time_in = []                                       # for generating output
        self.time_out = []                                      # for generating output
    
    def canServe(self):
        return not self.serving # should be not as it can't serve when it's serving
    
    def serve(self, lot):
        if (self.canServe()):
            self.serving = True
            self.lotid_list.append(lot.id)
            recipe = lot.sequenced_flow.popleft()
            self.recipe_list.append(recipe.id)
            self.time_in.append(datetime.now())
            self.time_out.append(datetime.now()+timedelta(days=recipe.process_time))
        return self, lot

    def addToQueue(self, lot):
        if (self.canServe()):
            self.queue.append(lot)
        return self
    
    def getFutureEventList(self):
        df = pd.DataFrame({
            'LotID': self.lotid_list,
            'Recipe': self.recipe_list,
            'Time_In': self.time_in,
            'Time_Out': self.time_out
        })
        return df
