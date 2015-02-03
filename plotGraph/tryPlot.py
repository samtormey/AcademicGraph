import networkx as nx
import matplotlib.pyplot as plt
import json
import re
import numpy
import random

json_data = open('leaves_Perm_Race.json').read()
data = json.loads(json_data)
cnt = 0

index = {}

for dat in data:
    keys = index.keys()
    try:
        dat["base"]
    except KeyError:
        continue
    if dat["base"].upper() not in keys:
        index[dat["base"].upper()] = cnt
        cnt += 1
    keys = index.keys()
    refType1 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num1"][0]))
    refType1 = refType1.group(0)
    refType2 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num2"][0]))
    refType2 = refType2.group(0)
    refType3 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num3"][0]))
    refType3 = refType3.group(0)
    refType4 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num4"][0]))
    refType4 = refType4.group(0)
    refType5 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num5"][0]))
    refType5 = refType5.group(0)
    if refType1 not in keys:
        index[refType1] = cnt
        cnt += 1
    keys = index.keys()
    if refType2 not in keys:
        index[refType2] = cnt
        cnt += 1
    keys = index.keys()
    if refType3 not in keys:
        index[refType3] = cnt
        cnt += 1
    keys = index.keys()
    if refType4 not in keys:
        index[refType4] = cnt
        cnt += 1
    keys = index.keys()
    if refType5 not in keys:
        index[refType5] = cnt
        cnt += 1




G = [[0.0 for x in range(cnt)] for x in range(cnt)]
yo = 0

counter = 1

for dat in data:
    print counter 
    counter += 1
    try:
        dat["base"]
    except KeyError:
        continue
    refType1 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num1"][0]))
    refType1 = refType1.group(0)
    numCite1 =  re.search(r'\d*,?\d+', str(dat["field_num1"][0]))
    numCite1 = int(numCite1.group(0).replace(",", ""))
    G[index[dat["base"].upper()]][index[refType1]] += numCite1

    refType2 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num2"][0]))
    refType2 = refType2.group(0)
    numCite2 =  re.search(r'\d*,?\d+', str(dat["field_num2"][0]))
    numCite2 = int(numCite2.group(0).replace(",", ""))
    G[index[dat["base"].upper()]][index[refType2]] += numCite2

    refType3 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num3"][0]))
    refType3 = refType3.group(0)
    numCite3 =  re.search(r'\d*,?\d+', str(dat["field_num3"][0]))
    numCite3 = int(numCite3.group(0).replace(",", ""))
    G[index[dat["base"].upper()]][index[refType3]] += numCite3

    refType4 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num4"][0]))
    refType4 = refType4.group(0)
    numCite4 =  re.search(r'\d*,?\d+', str(dat["field_num4"][0]))
    numCite4 = int(numCite4.group(0).replace(",", ""))
    G[index[dat["base"].upper()]][index[refType4]] += numCite4

    refType5 = re.search(r'[A-Z]+(\s[A-Z]+)*',  str(dat["field_num5"][0]))
    refType5 = refType5.group(0)
    numCite5 =  re.search(r'\d*,?\d+', str(dat["field_num5"][0]))
    numCite5 = int(numCite5.group(0).replace(",", ""))
    G[index[dat["base"].upper()]][index[refType5]] += numCite5



temp = numpy.array(G)
tempInd = numpy.where(temp != 0)
inv_index = {v: k for k, v in index.items()}
labels={}
Shw=nx.Graph()

#for i in range(cnt):  # add all nodes
    #Shw.add_node(i, subject=inv_index[i])
    #labels[i] = inv_index[i][0:4]


for i in range(cnt-1):  # Average the symmetric elements and make matrix symmetric
    for j in range(i+1,cnt):
        G[i][j] = (G[i][j] + G[j][i])/2
        G[j][i] = G[i][j]


for i in range(cnt):  # Normalize rows
    summedi = numpy.sum(G[i])
    if summedi != 0:
        for j in range(cnt):
            G[i][j] = G[i][j]/summedi

itr = 0
tempHolder = 0
desired = 0

print inv_index


for i in range(cnt):
    if G[desired][i] != 0:
        Shw.add_node(i)
        labels[i] = inv_index[i]
        Shw.add_edge(desired,i)
        theta = random.random()*2*numpy.pi
        r = pow(1-G[desired][i],7)
        Shw.node[i]['pos'] = (r*numpy.cos(theta),r*numpy.sin(theta))

labels[desired] = inv_index[desired]
Shw.node[desired]['pos'] = (0,0)

#for i in tempInd[0]:  # make edges in Shw (the graph we will display)
    #tempHolder = tempInd[1][itr] 
    #Shw.add_edge(i,tempHolder,dist=G[i][tempHolder])
    #itr += 1


pos = nx.get_node_attributes(Shw,'pos')
nx.draw(Shw,pos)
nx.draw_networkx_labels(Shw,pos,labels,font_size=6)
plt.show()
