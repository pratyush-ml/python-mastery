import os
import sys

class Stock:
    def __init__(self,names, shares,price):
        self.names = names
        self.shares = shares
        self.price = price
    def cost(self):
        return self.price * self.shares
