class PartNum:
    def __init__(self, id, sequenced_flow):
        self.id = id                            # String
        self.sequenced_flow = sequenced_flow    # List<Recipe>

    def getId(self):
        return self.id
    
    def getFlow(self):
        return self.sequenced_flow
    