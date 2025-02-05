import queue
from datetime import datetime, timedelta
import pandas as pd

class Machine:
    def __init__(self, id, recipes, location, curr_time):
        self.id = id                                            # String
        self.recipes = recipes                                  # List<Recipe>
        self.curr_recipe = ''                                   # default empty string
        self.serveEnd = 0
        self.pq = queue.PriorityQueue()                         # PQ<Lot>
        self.lotid_list = []                                    # for generating output
        self.recipe_list = []                                   # for generating output
        self.time_in = []                                       # for generating output
        self.time_out = []                                      # for generating output
        self.state = 'NOWIP'                                    # machine state (available for manufacturing or not)
        self.location = location                                # String
        self.child = []                                         # list to store chambers/child
        self.curr_time = curr_time                              # current time of simulation in seconds
    
    def getState(self):
        return self.state
        
    def addChild(self, child_machine):
        self.child.append(child_machine)

    def getChild(self):
        return self.child
    
    def canServe(self):
        return self.curr_time >= self.serveEnd
    
    def serve(self, lot, process_time):
        if (self.canServe()):
            recipe = lot.getNextRecipe()
            self.lotid_list.append(lot.getId())
            self.recipe_list.append(recipe.getId())
            self.time_in.append(self.curr_time)
            self.time_out.append(self.curr_time + process_time)

    def addToQueue(self, lot):
        if (self.canServe()):
            self.pq.put(lot)
    
    def getFutureEventList(self):
        df = pd.DataFrame({
            'LotID': self.lotid_list,
            'Recipe': self.recipe_list,
            'Time_In': self.time_in,
            'Time_Out': self.time_out
        })
        return df
