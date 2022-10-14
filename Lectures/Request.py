import requests
x = requests.get('https://www.yahoo.com/ads.txt')
text=x.text.split('\n')

dict={}
c=0
for i in text:
    if 'pubmatic.com' in i:
        c+=1
        line=i.split(',')
        line[2]=line[2].split()[0].strip().upper()     
        if line[2] not in dict.keys():
            dict[line[2]]=1
        else:
            dict[line[2]]+=1

print("total lines: ",c)
print(dict)