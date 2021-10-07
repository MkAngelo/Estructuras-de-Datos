import random

class Market:

    def __init__(self, elements):
        self.items = list()
        for i in range(elements):
            self.items.append(i + 1)
    
    def __str__(self):
        return str(self.items)

    def __total__(self):
        ans = 0
        for i in self.items:
            ans += int(i)
        return ans
    