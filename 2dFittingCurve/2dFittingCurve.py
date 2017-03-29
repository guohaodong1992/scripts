import xlrd
import sys
import numpy as np
import matplotlib.pyplot as plt
import json
import argparse
import os

# Arguments Parse
parser = argparse.ArgumentParser(description='Input Config File')
parser.add_argument('-c', '--config', help='configuration file in JSON')
args = parser.parse_args()
if args.config:
	print("> config file location: "+args.config)
else:
	print("> cannot run without config file, more help with --help")
	sys.exit(0)

# Configuration File Load
configFile = os.getcwd()+args.config
with open(configFile) as data_file:    
    conf = json.load(data_file)

fileName = conf['fileName']+".png"
xLabel = conf['xAxis']['name']
xCol = conf['xAxis']['xCol']
xRow = conf['xAxis']['xRow']
yLabel = conf['yAxis']['name']
yCol = conf['yAxis']['yCol']
yRow = conf['yAxis']['yRow']
title = conf['title']

# Input Data Load
data = xlrd.open_workbook(conf['xlsxFile'])
table = data.sheets()[0]

x = [0.0]*len(xRow)
y = [0.0]*len(yRow)
for i in range(0, len(xRow)):
	x[i] = float(table.row(xRow[i])[xCol].value)
	y[i] = float(table.row(yRow[i])[yCol].value)
print(x)
print(y)

z = np.polyfit(x, y, 3)
f = np.poly1d(z)

# Calculate Fitting Curve
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x, y, 'r--')
plt.plot(x, y, 'ko', x_new, y_new)
plt.xlim([x[0]-1, y[-1] + 1 ])
plt.title(title)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.savefig(fileName, dpi=100)
plt.show()
