class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        return self.lower > self.upper
    
    def contains(self, value):
        return self.lower <= value <= self.upper
    
    def overlaps_with(self, other):
        return self.lower <= other.upper and self.upper >= other.lower

