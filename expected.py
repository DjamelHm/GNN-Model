import json

with open('./data/test/data.json') as json_file:
    data = json.load(json_file)
    cpt=0
file = open('expected.txt','w')
for j in range(len(data)):
  for i in data[j]['nodes']:
    label=list(i.values())[0]
    if label!='ip':
       file.write(str(label)+"\n") 
       cpt+=1
file.close()
