#Convert AAVSO text files to csv 
#Author: Jeffrey C. Rombough
#Company: RCSCS
#20220620
#Note the standard list of imported functions can be found at https://docs.python.org/3/library/

#format of AAVSO files starts with 4 lines of garbage ASCII letters
#This is followed by 14 numbers delimited with one or more spaces
#There are 31 rows per file. Nulls can be counted at '0' 
#The yearly means and other information after the 31st row is not needed.

import sys

source = sys.argv[1]
destination = sys.argv[2]

#Open source file
sourceFile = open (source, 'r')
#fileLineNumbers = enumerate(sourceFile.readlines())



lineCounter = 0

while lineCounter < 35:
    line = sourceFile.readline()
    print("Line{}: {}".format(lineCounter, line))
    lineCounter += 1
    # The above shows the only way to increment in python x++ won't work
    # line number and content

sourceFile.close()

#destFile = 
#Create and open destination csv file
#Goto the 5th row
# Copy Number from source to destination. Use newlines on both. This could be a for loop with 31 iterations
# close both files



