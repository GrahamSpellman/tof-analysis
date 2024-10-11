import pandas as pd
import os
from matplotlib import pyplot as plt

data_path = os.getcwd() + "/data/"
figs_path = os.getcwd() + "/figs/"

frames = []

for filename in os.listdir(data_path):
    file_path = os.path.join(data_path, filename)
    df = pd.read_csv(file_path, header=4, sep='\t')
    frames.append(df)

fig, ax = plt.subplots()
ax.plot(frames[0].iloc[:,0],frames[0].iloc[:,3])
plt.show()