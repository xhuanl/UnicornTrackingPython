'''
SearchResult class represents the final result to be printed.

Created on Jul 1, 2017

@author: xhuan
'''

class searchResult():
    
    def __init__(self, s):
        self.result = []
        self.maxSize = s

    '''
    Using an algorithm similar to insertion sort
    to store the qualified points. 
    '''
    def add(self, p):
        
        if p is None:
            return
        
        if len(self.result) == 0:
            self.result.append(p)
            return
        
        '''
         If the expected number of point is not filled and 
         the distance to the new point is greater the longest 
         distance we have currently, add the new point as the
         last element. Otherwise drop the point.
        '''
        if p.distanceSquare >= self.result[-1].distanceSquare:
            if (len(self.result) < self.maxSize):
                self.result.append(p)
            return
        
        i = len(self.result) - 1
        
        if len(self.result) < self.maxSize:
            self.result.append(self.result[-1])
        
        '''
        Similar to the Insertion sort, if the distance to the new point is 
        between the distances of the existing points, insert the new point
        to the array with proper order.
        '''    
        while i > 0 and p.distanceSquare < self.result[i].distanceSquare:
            self.result[i] = self.result[i - 1]
            i = i - 1
        
        self.result[i] = p
        
        return
    
