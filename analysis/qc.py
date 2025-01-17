import numpy as np

degree = []
with open('degree.log', 'r') as logfile:
    for line in logfile:
        columns = line.split()
        if len(columns) >= 1:
            dg = float(columns[2])
            degree.append(dg)
    print(degree)

yed = []
with open('yield.log', 'r') as logfile:
    for line in logfile:
        columns = line.split()
        if len(columns) >= 1:
            yd = float(columns[1])
            yed.append(yd)
    print(yed)

mylog = open('qc.log', 'w')
print(np.array(degree) / np.array(yed), file = mylog)
