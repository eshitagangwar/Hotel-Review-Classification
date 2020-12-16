def read_data_label(filename):
    a = ''
   
    if 'negative_polarity/deceptive' in filename:
        a = 'negative_deceptive'
    elif 'negative_polarity/truthful' in filename:
        a = 'negative_truthful'
    elif 'positive_polarity/deceptive' in filename:
        a = 'positive_deceptive'
    elif 'positive_polarity/truthful' in filename:
        a = 'positive_truthful'
    
    
    file1 = open(filename,'r')
    k = file1.read().replace('\n',' ')
    
    return [a ,k]
        

    
import math
import os
from os import walk
import sys
import re
train_data = []
input_path = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(next(os.walk(input_path))[0]):
    for f in filenames:
        file_name = os.path.join(dirpath, f)
        if bool(re.search('.txt',file_name)):
            train_data.append(read_data_label(file_name))
f = open('try.txt','r')
stopwords = set(f.read().replace('\n',' ').split(' '))


def remove_stopwords(i):
    ans = []
    cleaned_str=re.sub('[^a-z\s]+',' ',i,flags=re.IGNORECASE) 
    cleaned_str=re.sub('(\s+)',' ',cleaned_str) 
    i=cleaned_str.lower()
    
    i = i.split(' ')
    for j in i:
        if j not in stopwords:
            j = j.lower()
            ans.append(j)
    return ans

common_dict = {'negative_deceptive': {},'positive_truthful':{} ,'negative_truthful':{} ,'positive_deceptive':{}}
number_of_element  = {'negative_deceptive': 0,'positive_truthful':0 ,'negative_truthful':0 ,'positive_deceptive':0}

unique_words = set()
for i in train_data:
    data = i[1]
    data_label = i[0]
    number_of_element[data_label] += 1
    clean = remove_stopwords(data)
    for j in clean:
        unique_words.add(j)
        if j in common_dict[data_label]:
            common_dict[data_label][j] +=1
        else:
            common_dict[data_label][j] =1
            
    


de = sum(number_of_element.values())
for i in number_of_element:
    number_of_element[i] = math.log(number_of_element[i]/de)
number_of_element

total = {}
for i in common_dict:
    total[i] = sum(common_dict[i].values())

for i in unique_words:
    for j in common_dict:
        if i not in common_dict[j]:
            common_dict[j][i] = 1
        else:
            common_dict[j][i] = common_dict[j][i]+1
        num = common_dict[j][i]
        dem = total[j]+len(unique_words)+1
        common_dict[j][i] = math.log(num/dem) 
        
        
result  = {"pro_each_class" :number_of_element, 'probability_score' : common_dict}
with open('nbmodel.txt', 'w') as file:
    file.write(str(result).replace("'", "\""))
    file.close()