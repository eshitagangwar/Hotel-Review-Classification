import math
import os
from os import walk
import operator
import re
import sys
import json
def param():
    
    
    with open('nbmodel.txt') as json_file:
        data = json.load(json_file)
        number_of_element = data["pro_each_class"]
        common_dict = data['probability_score'] 
        return  (common_dict , number_of_element)



def read_data_label(filename):
    
    
    
    file1 = open(filename,'r')
    k = file1.read().replace('\n',' ')
    
    return [k,filename]
        

    

train_data = []
input_path = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(next(os.walk(input_path))[0]):
    for f in filenames:
        file_name = os.path.join(dirpath, f)
        if bool(re.search('.txt',file_name)):
            train_data.append(read_data_label(file_name))
f = open('try.txt','r')
stopwords = set(f.read().replace('\n',' ').split(' '))
common_dict , number_of_element = param()




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


def check_f(a):
    c =0
    return_ans = ''
    for test in a:
        ans = ''
        pre =remove_stopwords(test[0])
        file  = test[1]
        ap = {}
        ap['negative_deceptive'] = number_of_element['negative_deceptive']
        ap['negative_truthful'] = number_of_element['negative_truthful']
        ap['positive_truthful'] =  number_of_element['positive_truthful']
        ap['positive_deceptive'] = number_of_element['positive_deceptive']
        for i in pre:
            for j in common_dict:
                if i in common_dict[j]:
                    ap[j] += common_dict[j][i]
                
                    
            
                

        label = test[0]
        ans = max(ap.items(), key=operator.itemgetter(1))[0]
        if label == ans:
            c= c+1
        ans  = str(ans.split('_')[1])+ ' '+ str(ans.split('_')[0]) + ' ' + str(file) + '\n'
        return_ans += ans
        
        
    return(return_ans , c/len(train_data))
return_ans , c =check_f(train_data)
with open('nboutput.txt', 'w') as file:
    file.write(str(return_ans))
    file.close()