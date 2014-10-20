import pandas as pd
import pickle
import numpy as np
import os, json, requests
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.realpath(__file__)));
print os.getcwd();
frame = pd.read_csv("Cars93.csv");

#Since rotary was the only value that wasn't a number, made rotoary set to 0
mapping = {'rotary':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8'};
frame.Cylinders = frame['Cylinders'].map(mapping);

#Since 0 and 1 are easier to work with
mapping = {'non-USA':'0','USA':'1'}
frame['Origin'] = frame['Origin'].map(mapping);

#Since 0 and 1 are easier to work with
mapping = {'Yes':'0','No':'1'}
frame['Man.trans.avail'] = frame['Man.trans.avail'].map(mapping);

print frame.describe()


fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
plt.scatter(frame['Price'], frame['Horsepower'])
ax2 = fig.add_subplot(2, 2, 2)
plt.plot(frame['Man.trans.avail'], frame['MPG.highway'])
ax3 = fig.add_subplot(2, 2, 3)
plt.scatter(frame['Price'], frame['MPG.highway'])

with open("Cars93.pickle", "wb") as scores:
    pickle.dump(fig, scores)
