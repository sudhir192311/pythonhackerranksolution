solved question solutions


import math
import os
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    
    # Write your code here
    # using count fuction
    results=[]
    for i in queries:
        results.append(strings.count(i))
    return results 
   # or without using function  
    for i in range(len(queries)):
       counter=0
       for j in range(len(strings)):
           if queries[i]== strings[j]:
                counter+=1
    results.append(counter) 
    return results 
   
      
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
