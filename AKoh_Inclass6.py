#Andrew Koh
#10/12/2014
#Inclass6

import pandas as pd
import requests
r = requests.get('http://api.github.com/events')
r

t = r.json()

t1 = pd.read_table('stress2_1.txt')

data_fr = pd.DataFrame(t, t1)
data_fr.to_pickle('inclass6_pickle')
data_fr.to_pickle('inclass6_pickle')

store = pd.HDFStore('mydata.h5')
store['obj1'] = data_fr
store['obj1']

t2 = pd.read_csv('Cars93.csv')
t2.describe()
bins = ['small', 'midsize', 'large', 'sporty', 'compact', 'Van']

category = pd.cut(t2.Type, bins)
freq = pd.value_counts(category)

t2.rename(t2.Type, "size")
t2.rename(t2.Manufacturer, "Company")

samp1 = t2.random.permutation(39)
samp2 = t2.random.permutation(39)

df3 = pd.merge(samp1, samp2, on='size')

df3.drop_duplicates()#.8 remaining
