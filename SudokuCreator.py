from array import *

rows, cols = (9, 9)
arr=[]
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(0)
    arr.append(col)
for row in arr:    
    print(row)