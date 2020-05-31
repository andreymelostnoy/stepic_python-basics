class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if self.money + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v) is True:
            self.money += v
