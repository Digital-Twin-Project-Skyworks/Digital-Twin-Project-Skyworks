import pandas as pd
#from ../Data import recptime_active_version

class PartNum:
    def __init__(self, id, sequenced_flow):
        self.id = id                            # String
        self.sequenced_flow = sequenced_flow    # List<Recipe>
        self.tct = self.calculate_tct()         # Integer in seconds

    def getId(self):
        return self.id
    
    def getFlow(self):
        return self.sequenced_flow
    
    def getTCT(self):
        return self.tct
    
    def calculate_tct(self):
        tct = 0
        df = pd.read_csv('Data/recptime_active_version.csv')

        for recp in self.sequenced_flow:
            try:
                recptime = df.loc[df['recpname'] == recp, 'mean'].values[0]
            except IndexError:
                recptime = 0
            tct += recptime

        return tct
