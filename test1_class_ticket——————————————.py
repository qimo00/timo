class Ticket():
    fee = 100
    weekend = [6, 7]
    def __init__(self, week_in, child):
        self.week_in = week_in
        self.child = child

        if week_in in self.weekend:
            self.fee = self.fee * 1.2

        if child == True :
            self.fee = self.fee *0.5

    def fee_g(self):
        return self.fee


