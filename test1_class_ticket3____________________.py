class Ticket():
    def __init__(self, weekend = False, child = False):
        self.fee = 100
        if weekend :
            self.inc = 1.2
        else:
            self.inc = 1.0
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calprice(self, num):
        return self.fee * self.inc *self.discount * num

man = Ticket()
child = Ticket(child=True)

print(man.calprice(3)+child.calprice(2))
