'''
Search all the points imported from the input file 
to find the required number of the closest points.
 
Created on Jul 1, 2017

@author: xhuan
'''
from point import point
from searchResult import searchResult

class search():
    
    def __init__(self, inpt, out, p, s):
        self.inputFile = inpt
        self.outputFile = out
        self.centraPoint = p
        self.result = searchResult(s)
    
    '''
    Read the input file and add the points to the array 
    if its distance to the central point is close.
    '''
    def processInputFile(self):
        
        file = open(self.inputFile, 'r')
        
        for line in file:
            if len(line) == 0:
                continue
            
            p = point()
            
            if p.parse(line):
                p.distanceSquare = p.distanceSquareFrom(self.centraPoint)
                self.result.add(p)

    '''
    Output the result to a file.
    '''
    def printResult(self):

        if len(self.result.result) == 0:
            return
        
        file = open(self.outputFile, 'w+')

        for p in self.result.result:
            file.write("(" + str(p.cords[0]) + ", " + str(p.cords[1]) + ", " + str(p.cords[2]) + ")\n")

