#Andrew Koh
#10/07/2014
#Inclass5

import pandas
import numpy
import matplotlib

#?pandas.eval()
#?pandas.e*
#?pandas.melt
#?pandas.lib
#?pandas.json

#?numpy.e*
#?numpy.emath
#?numpy.equal
#?numpy.errstate
#?numpy.empty

#?matplotlib.f*
#?matplotlib.figure
#?matplotlib.finance
#?matplotlib.ft2font
#?matplotlib.get_backend



#?cumsum - returns a cumulative sum of the elements along a given axis
numpy.random.uniform(low=0.1, high=1.0, size=100) #100000000 loops, best of 3: 10.1 ns per loop
numpy.random.uniform(low=0.1, high=1.0, size=1000) #100000000 loops, best of 3: 10.1 ns per loop
numpy.random.uniform(low=0.1, high=1.0, size=10000) #100000000 loops, best of 3: 10.1 ns per loop


#part 2
array1 = [0, 1, 2, 3, 4]
print array1
print "array1 is 1 line and integer"
array2 = [0, 1, 2, 3, 4]
print array2
print "array2 is 1 line and integer"

#part 3
total = numpy.sum([array1, array2])

#part 4
product = numpy.prod([array1, array2])

#part 5
identity = numpy.identity(6)

#part 6 assuming matrix[row][col]
col = 0
while col < 6:
    identity[3][col] = 5
    col = col + 1

#part 7 
for i in range(0, 6): 
    for j in range(0, 6):
        if identity[i][j] != 0:
            identity[i][j] = 6
        
#part 8 
arr3 = [[0, 1],[1, 3, 5],[2, 6, 1, 6]]

#part 9 
print arr3
print "arr3 is 3 dimensional rectangular prism with integer type"

#part 10 
arr3 = [[5, 1],[1, 5, 5],[2, 5, 1, 6]]

#part 11
arrayRandom = numpy.random.uniform(low=0.1, high=1.0, size=20)

#part 12
minOfRandom = arrayRandom[0]
maxOfRandom = arrayRandom[0]
sumOfRandom = 0
for i in arrayRandom:
    if i < 19:
        minOfRandom = min(minOfRandom, arrayRandom[i + 1])
        maxOfRandom = max(maxOfRandom, arrayRandom[i + 1])
    if i <= 19:
        sumOfRandom = sumOfRandom + arrayRandom[i]
meanOfRandom = sumOfRandom / 20

#part 13 
for i in arrayRandom:
    if arrayRandom[i] > 5:
        arrayRandom[i] = 1
    else:
        arrayRandom[i] = 0
        
#part 14
arrayRandom = sorted(arrayRandom)

#part 15
unique = set(arrayRandom)
print unique

#part 16 "comments delimiting all your code and output"


import Quandl
bitstamp = Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="iosLM_LP3SAsEAbdxKxC")
bitfinex = Quandl.get("BCHARTS/BITFINEXUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="iosLM_LP3SAsEAbdxKxC")
lakebtc = Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="iosLM_LP3SAsEAbdxKxC")
bitstamp.head() #columns are open, high, low, close, volume (BTC), volume (Currency), Weighted Price
bitfinex.head() #columns are open, high, low, close, volume (BTC), volume (Currency), Weighted Price
lakebtc.head() #columns are open, high, low, close, volume (BTC), volume (Currency), Weighted Price
ind1 = bitstamp #273 x 7
ind2 = bitfinex #273 x 7
ind3 = lakebtc #214 x 7

#7 columns in each of the datasets  
