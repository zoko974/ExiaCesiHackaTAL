#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

import matplotlib.patches as mpatches
import os

MOT = sys.argv[1]

annees = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
Domaines = {'A':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'G':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'H':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
DomainesTotal ={'A':[0],'G':[0],'H':[0]}


type_num = {"abstract":1,"claims":2,"description":3}
values_domain = {"A":{"color":'r', "label":"Human necessities"},"G":{"color":'b', "label":"Physics"},"H":{"color":'g', "label":"Electricity"}}

MAIN_DIR = os.getcwd()
os.chdir(MAIN_DIR)

with open('mots.json', 'rU') as json_data:
	cube = json.load(json_data)
json_data.close()
for annee in cube[MOT]:
	for domaine in cube[MOT][annee]:
		for type_name in cube[MOT][annee][domaine]:
			#ax.scatter(int(annee), type_num[type_name], cube[MOT][annee][domaine][type_name], c=values_domain[domaine]["color"], marker='o')
			Domaines[domaine][int(annee)-2000] = Domaines[domaine][int(annee)-2000] + cube[MOT][annee][domaine][type_name]
			DomainesTotal[domaine][0]=Domaines[domaine][0]+cube[MOT][annee][domaine][type_name]




print Domaines




# bins = [x + 1 for x in range(0, 17)]
#plt.hist([Domaines['A'], Domaines['G'],Domaines['H']], bins = 18, color = ['yellow', 'green' , 'blue'],
#            edgecolor = 'red',  label = ['Human necessities', 'Physics', 'Electricity'],
#            histtype = 'barstacked')

barWidth = 0.8
y1 = Domaines['A']
y2 = Domaines['G']
y3 = Domaines['H']
r = range(len(y1))




plt.figure(figsize=(12,7))

plt.bar(r, y1, width = barWidth, color = ['yellow' for i in y1],
           edgecolor = ['blue' for i in y1], linestyle = 'solid', hatch ='/',
           linewidth = 3)
plt.bar(r, y2, width = barWidth, bottom = y1, color = ['pink' for i in y1],
           edgecolor = ['green' for i in y1], linestyle = 'solid', hatch = '/',
           linewidth = 3)
plt.bar(r, y3, width = barWidth, bottom = y1, color = ['orange' for i in y1],
           edgecolor = ['red' for i in y1], linestyle = 'solid', hatch = '/',
           linewidth = 3)
plt.xticks([r + barWidth / 2 for r in range(len(y1))], ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])



plt.ylabel('Valeur')
plt.xlabel('Quantite')
plt.title('Histogramme empile :'+MOT)

Domaine1 = mpatches.Patch(color='yellow', label='Human necesities')
Domaine2 = mpatches.Patch(color='pink', label='Physics')
Domaine3 = mpatches.Patch(color='orange', label='Electricity')
plt.legend(handles=[Domaine1,Domaine2,Domaine3])




plt.title("Utilisation du mot "+MOT+" par domaine")


plt.show()