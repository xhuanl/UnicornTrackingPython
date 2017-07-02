'''
A program to show the closest number of points from the given point.

Created on Jul 1, 2017

@author: xhuan
'''
import os
import argparse
from point import point
from search import search

def main(inputFile, outputFile, targetPoint, count):
    s = search(inputFile, outputFile, targetPoint, count)

    s.processInputFile()
    s.printResult()
    
    print("Finished tracking.")

# Entry point of the application.
if __name__=='__main__': 

    # Parse the input.
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='inputFile')
    parser.add_argument('-p', '--point', dest='centralPoint')
    parser.add_argument('-c', '--count', dest='count')
    parser.add_argument('-o', '--output', dest='outputFile')
    args = parser.parse_args()
    
    inputFile = args.inputFile
    centralPoint = args.centralPoint
    count = args.count
    outputFile = args.outputFile

    if not inputFile:
        print("Missing input file path.")
        os._exit(1)
    
    if not centralPoint:
        print("Missing the designated point.")
        os._exit(1)
    else:
        p = point()

        if not p.parse(centralPoint):
            print("Missing the designated point.")
            os._exit(1)

    if not count:
        print("Missing the expected amount of locations.")
        os._exit(1)
    else:
        c = int(count)
                
    if not outputFile:
        print("Missing input file path.")
        os._exit(1)

    # Run the program.
    main(inputFile, outputFile, p, c)