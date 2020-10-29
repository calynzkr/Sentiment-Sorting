#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import re
from collections import Counter
from collections import defaultdict
df = pd.read_csv("/Users/calyn/Documents/Fall 2020/595/Sentiment Sorting/mergedresult.csv",usecols = ['Purpose'])
data_set= df.to_string()
data_set

#split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered input values and their respective counts. 
most_occur = Counter.most_common(4) 
  
print(most_occur)

