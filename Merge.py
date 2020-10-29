#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import glob
import pandas as pd


path = "/Users/calyn/Documents/Fall 2020/595/Sentiment Sorting"


all_files = glob.glob(os.path.join(path, "company*.csv"))
header_saved = False
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "mergedresult.csv")

