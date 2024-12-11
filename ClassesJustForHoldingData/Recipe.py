class Recipe:
    def __init__(self, id, process_time, toolswap_time):
        self.id = id                        # String
        self.process_time = process_time    # String
        self.toolswap_time = toolswap_time  # String

    def getId(self):
        return self.id
    
    def getProcessTime(self):
        return self.process_time
    
    def getToolswapTime(self):
        return self.toolswap_time
    