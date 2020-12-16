#!/usr/bin/env python
# coding: utf-8

# In[3]:

import sys
import math
import os
from os import walk
import re
import random
import json
from random import shuffle
def read_data_label(filename):

    
    if 'negative' in filename:
        a1 = 'negative'
    else:
        a1 = 'positive'
    if  'truthful' in filename:
        a2 = 'truthful'
    else:
        a2 = 'deceptive'
    
    file1 = open(filename,'r')
    k = file1.read().replace('\n',' ')
    
    return [k,a1,a2]
        

  


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
input_path = sys.argv[1]

for (dirpath, dirnames, filenames) in walk(next(os.walk(input_path))[0]):
    for f in filenames:
        file_name = os.path.join(dirpath, f)
        if bool(re.search('.txt',file_name)):
            train_data.append(read_data_label(file_name))
f = open('stop.txt','r')
stopwords = set(f.read().replace('\n',' ').split(' '))
td = {'truthful':1, 'deceptive':-1}
pn = {'positive':1, 'negative':-1 }
pn_w = {'w0' : 0}
td_w = {'w0' : 0}

avg_pn_w = {'w0' : 0}
avg_dt_w = {'w0' : 0}

cached_weight_pn  = {'w0' : 0}
cached_weight_dt = {'w0' : 0}


count=1

for i in range(100):
    random.shuffle(train_data) 
    for data in train_data:
        text = data[0]
        a1 = data[1]
        a2 = data[2]
        words = remove_stopwords(text)
        pn_y = pn_w['w0']
        td_y = td_w['w0']
        avg_pn_y = avg_pn_w['w0']
        avg_td_y = avg_dt_w['w0']
        b1 = 0
        b2 = 0
        for k in words:
            if k not in pn_w:
                pn_w[k] = 0
            if k not in avg_pn_w:
                avg_pn_w[k] = 0
            if k not in cached_weight_pn:
                cached_weight_pn[k] = 0
            if k not in td_w:
                td_w[k] = 0
            if k not in avg_dt_w:
                avg_dt_w[k] = 0
            if k not in cached_weight_dt:
                cached_weight_dt[k] = 0

        
        for k in words:
            pn_y += words[k] * pn_w[k]
            td_y += words[k] * td_w[k]
            avg_pn_y += words[k] * avg_pn_w[k]
            avg_td_y += words[k] * avg_dt_w[k]
        mul_1 = pn_y*pn[a1]
        mul_2 = td_y*td[a2]
        mul_3 = avg_pn_y*pn[a1] 
        mul_4 = avg_td_y*td[a2]
        if mul_1 <= 0:
            pn_w['w0'] += pn[a1]
            for k in words:
                pn_w[k] += pn[a1] * words[k]
            
        
        if mul_2 <= 0:
            td_w['w0'] += td[a2]
            for k in words:
                td_w[k] += td[a2] * words[k]
            
        
        if mul_3 <= 0:
            cached_weight_pn ['w0'] += pn[a1] * count
            avg_pn_w['w0'] += pn[a1]
           
            for k in words:
                avg_pn_w[k] += pn[a1] * words[k]
                cached_weight_pn [k] += pn[a1] * count * words[k]
            
            
        
        if mul_4 <= 0:
            cached_weight_dt['w0'] += td[a2] * count
            avg_dt_w['w0'] += td[a2]
           
            for k in words:
                avg_dt_w[k] += td[a2] * words[k]
                cached_weight_dt[k] += td[a2] * count * words[k]
             
            

        count = count+1

for x  in avg_pn_w:
    if x  in cached_weight_pn :
        avg_pn_w[x] -= cached_weight_pn [x]/(count)
    

for x  in avg_dt_w:
    if x  in cached_weight_dt:
        avg_dt_w[x] -= cached_weight_dt[x]/(count)
    


vanilla = {'pos_neg': pn_w, 'tru_dec': td_w}
averaged = {'pos_neg': avg_pn_w, 'tru_dec': avg_dt_w}


with open('vanillamodel.txt','w') as file:
    file.write(str(vanilla).replace("'", "\""))
    file.close()

with open('averagedmodel.txt','w') as file:
    file.write(str(averaged).replace("'", "\""))
    file.close()

