import pandas as pd
import glob
import os

path = "c:/Users/xyz/Desktop/files"

allFiles = glob.glob(os.path.join(path,"*.csv"))
frame = pd.DataFrame
list_ = []

for file_ in allFiles:
  df = pd.read_csv(file_,index_col=None,header=None)
  list_.append(df)
  
frame = pd.concat(list_)

frame.to_csv("c:/Users/xyz/Desktop/files",sep = '\t')
