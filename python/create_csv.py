import pandas as pd
import numpy as np

df = pd.read_pickle("../data/semiconductor/LSWMD.pkl")
def find_dim(x):
    dim0=np.size(x,axis=0)
    dim1=np.size(x,axis=1)
    return dim0,dim1

df['waferMapDim']=df.waferMap.apply(find_dim)

df['failureNum']=df.failureType
df['trainTestNum']=df.trianTestLabel
mapping_type={'Center':0,'Donut':1,'Edge-Loc':2,'Edge-Ring':3,'Loc':4,'Random':5,'Scratch':6,'Near-full':7,'none':8}
mapping_traintest={'Training':0,'Test':1}
df=df.replace({'failureNum':mapping_type, 'trainTestNum':mapping_traintest})

df = df.drop(["trianTestLabel", "failureType"], axis=1)
df = df[df["failureNum"] != 8]
df = df.head(10000)

df.to_csv("../data/semiconductor/LSWMD.csv", index_label="id")
