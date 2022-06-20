#Python Data Tools Template
#Author: Jeffrey C. Rombough
#Company: RCSCS
#20220620
#Note the standard list of imported functions can be found at https://docs.python.org/3/library/

import sys

#Use argv for source and destination files names (or make them one and the same)
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
source = sys.argv[1]
destination = sys.argv[2]
print(source + " as source")
print(destination + " as destination")

#C:\mx\rcscs\PythonDataTools>python Convert_AAVSO_text_2_csv.py arg1 arg2
#This is the name of the script:  Convert_AAVSO_text_2_csv.py
#Number of arguments:  3
#The arguments are:  ['Convert_AAVSO_text_2_csv.py', 'arg1', 'arg2']

#https://www.knowledgehut.com/blog/programming/sys-argv-python-examples


