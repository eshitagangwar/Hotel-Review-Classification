#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math
import os
from os import walk
import operator
import os
import collections
import re
import json
import random
import sys


def read_data_label(filename):

  
    
    file1 = open(filename,'r')
    k = file1.read().replace('\n',' ')
    
    return [k,filename]
        

    




def remove_stopwords(i):
    ans = {}
    cleaned_str=re.sub('[^a-z\s]+',' ',i,flags=re.IGNORECASE) 
    cleaned_str=re.sub('(\s+)',' ',cleaned_str) 
    i=cleaned_str.lower()
    
    i = i.split(' ')
    for j in i:
        if j not in stopwords:
            j = j.lower()
            if j not in ans:
                ans[j] = 1
            else:
                ans[j] += 1
    return ans


train_data = []
model = sys.argv[1]
input_path = sys.argv[2]

for (dirpath, dirnames, filenames) in walk(next(os.walk(input_path))[0]):
    for f in filenames:
        file_name = os.path.join(dirpath, f)
        if bool(re.search('.txt',file_name)):
            train_data.append(read_data_label(file_name))
f = open('stop.txt','r')
stopwords = set(f.read().replace('\n',' ').split(' '))

weight = {'pos_neg':{} , 'tru_dec' :{}}
with  open(model,'r') as json_file:
        data = json.load(json_file)
        weight['pos_neg'] = data['pos_neg']
        weight['tru_dec'] = data['tru_dec']
        
return_ans = ''    
for d in train_data:
    file = d[0]
    words = remove_stopwords(file)
    pos_neg_bias = weight['pos_neg']['w0']
    tru_de_bias = weight['tru_dec']['w0']
    for word in words:
        if word in weight['tru_dec']:
            tru_de_bias += weight['tru_dec'][word]*words[word]
        if word in weight['pos_neg']:
            pos_neg_bias += weight['pos_neg'][word]*words[word]
        

    if tru_de_bias>=0:
        a1 = "truthful"
    elif tru_de_bias<0:
        a1 = "deceptive"
    
    if pos_neg_bias>=0:
        a2 = "positive"
    elif pos_neg_bias<0:
        a2 = "negative"
    
    ans  = a1+ ' '+ a2 + ' ' + str(d[1]) + '\n'
    return_ans += ans

with open('percepoutput.txt','w') as file:
    file.write(str(return_ans))
    file.close()
    

