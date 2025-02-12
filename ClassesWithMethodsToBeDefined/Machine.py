import pandas as pd

class Machine:
    def __init__(self, id, recipes, location):
        self.id = id                                            # String
        self.recipes = recipes                                  # List<Recipe>
        self.location = location                                # String
        self.child = []                                         # list to store chambers/child

        self.curr_recipe = ''                                   # default empty string
        self.serveEnd = 0
        self.fel = []                                           # for generating output

    def addChild(self, child_machine):
        self.child.append(child_machine)

    def getChild(self):
        return self.child
    
    def canServe(self, curr_time):
        return curr_time >= self.serveEnd
    
    def serve(self, lotid, recipe, curr_time, recipe_time):
        if (self.canServe()):
            self.curr_recipe = recipe
            self.serveEnd = curr_time + recipe_time
            self.fel.append([lotid, recipe, curr_time, curr_time + recipe_time])
    
    def getFutureEventList(self):
        column_names = ['LotID', 'Recipe', 'Time_In, Time_Out']
        df = pd.DataFrame(self.fel, columns=column_names)
        return df
