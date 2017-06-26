#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

import matplotlib.patches as mpatches
import os

print "test"

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



# Domaines['A']=[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]

# # bins = [x + 1 for x in range(0, 17)]
# plt.hist([Domaines['A'], Domaines['G'],Domaines['H']], bins = 18, color = ['yellow', 'green' , 'blue'],
#             edgecolor = 'red',  label = ['Humannecessities', 'Physics', 'Electricity'],
#             histtype = 'barstacked')


# plt.ylabel('Quantite')
# plt.xlabel('Annee')
# plt.title('Histogramme empile :'+MOT)
# plt.legend()



plt.figure(figsize = (8, 8))
x2 = [DomainesTotal['A'], DomainesTotal['G'],DomainesTotal['H']]
plt.pie(x2, labels = ['Humannecessities', 'Physics', 'Electricity'],
           colors = ['red', 'green', 'yellow'],
           explode = [0, 0, 0],
           pctdistance = 0.7, labeldistance = 1.4,
           shadow = True)
plt.legend()
plt.title("Utilisation du mot '"+MOT+"' par domaine")


plt.show()