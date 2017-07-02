'''
Point class to represent the points.

Created on Jul 1, 2017

@author: xhuan
'''
import re

class point():
    
    def __init__(self):
        self.cords = []
        self.distanceSquare = 0
        
    def parse(self, inpt):
        try:
            matcher = re.search('\\((.+)\\)', inpt)
            cords = matcher.group(0).strip('()').split(',')
        except:
            print("Invalid input: " + inpt)
            return False            
        
        if not len(cords) == 3:
            print("Invalid input: " + inpt)
            return False
        
        try:
            self.cords = [int(x) for x in cords]
        except:
            print('Invalid input: ' + inpt)
            return False
        
        return True
    
    def square(self, p):
        return [(self.cords[i] - p.cords[i])*(self.cords[i] - p.cords[i]) for i in range(3)]
    
    # Using the distance square to avoid the sqrt operation
    # and keep the integer result. 
    def distanceSquareFrom(self, p):
        return sum(self.square(p))
