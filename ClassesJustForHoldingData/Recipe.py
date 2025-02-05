class Recipe:
    def __init__(self, id, lower_bound, upper_bound):
        self.id = id                        # String
        self.lower_bound = lower_bound      # int
        self.upper_bound = upper_bound      # int

    def getId(self):
        return self.id
    
    def getLower(self):
        return self.lower_bound
    
    def getUpper(self):
        return self.upper_bound    