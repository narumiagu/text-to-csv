#%%
import os
import csv
from re import sub

def get_file_contents() -> list:
  path = './qans/'
  res = {}
  label = set()
  for file in os.listdir(path):
    with open(os.path.join(path,file),encoding='utf-8',mode='r') as f:
      for data in f:
        data = data.strip()
        line = f.readline().strip()
        if not data: continue
        #print('data,line ->',data,line)
        if '氏名' in data:
          if line not in res:
            name = line
            res[name] = {}
        if '科目' in data:
          subject = line
          if subject not in res[name]:
            res[name][subject] = {}
        if data[0] in ['1','2','3','4','5','6','7','8']:
          res[name][subject][data] = line
          label.add(data)
          continue
  return [label,res]

def write_csv(label,data):
  with open('result.csv',mode='w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    label = ['氏名','科目',] + sorted(label)
    writer.writerow(label)
    anks = []
    for k in data:
      #print(data[k])
      for j in data[k]:
        #print(j)
        ank = []
        for i in data[k][j]:
          print(data[k][j][i])
          ank.append(data[k][j][i])
        anks.append(ank)
          #writer.writerow([k,j]+ank)
    print(anks)
    writer.writerows(anks)
        #writer.writerow([data[k],j])

def main():
  t = get_file_contents()
  write_csv(t[0],t[1])

# %%
main()

# %%
