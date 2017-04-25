class Ticket():
    fee = 100
    def __init__(self, weekend = False, child = False):
        self.weekend = weekend
        self.child = child
        if self.child == True:
            self.fee = self.fee * 0.5
    def calfee(self, num):
        if self.weekend == True:
            self.fee = self.fee * 1.2
        return self.fee * num

    
