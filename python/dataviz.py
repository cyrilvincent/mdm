import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import json

df = pd.read_csv("../data/wafer/LSWMD.csv", index_col="id")

df_withlabel = df[(df['failureNum']>=0) & (df['failureNum']<=8)]
df_withlabel =df_withlabel.reset_index()
df_withpattern = df[(df['failureNum']>=0) & (df['failureNum']<=7)]
df_withpattern = df_withpattern.reset_index()
df_nonpattern = df[(df['failureNum']==8)]
print(df_withlabel.shape[0], df_withpattern.shape[0], df_nonpattern.shape[0])

fig = plt.figure()
gs = gridspec.GridSpec(1, 1)
ax2 = plt.subplot(gs[0])

tol_wafers = df.shape[0]
no_wafers=[tol_wafers-df_withlabel.shape[0], df_withpattern.shape[0], df_nonpattern.shape[0]]

colors = ['blue', 'green', 'red']

uni_pattern=np.unique(df_withpattern.failureNum, return_counts=True)
labels2 = ['','Center','Donut','Edge-Loc','Edge-Ring','Loc','Random','Scratch','Near-full']
ax2.bar(uni_pattern[0],uni_pattern[1]/df_withpattern.shape[0], color='green', align='center', alpha=0.9)
ax2.set_title("failure type frequency")
ax2.set_ylabel("% of pattern wafers")
ax2.set_xticklabels(labels2)

plt.show()

sub_df = df.loc[df['waferMapDim'] == "(26, 26)"]
sub_wafer = sub_df['waferMap'].values

sw = np.ones((1, 26, 26))
label = list()

for i in range(len(sub_df)):
    s = sub_df.iloc[i,:]['waferMap']
    s = s.replace(" ", ",")
    js = json.loads(s)
    map = np.array(js)
    sw = np.concatenate((sw, map.reshape(1, 26, 26)))
    label.append(sub_df.iloc[i,:]['failureNum'])

x = sw[1:]
y = np.array(label).reshape((-1,1))

plt.imshow(x[0])
plt.show()

