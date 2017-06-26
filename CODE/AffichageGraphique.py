#!/usr/bin/env python
'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

import matplotlib.patches as mpatches
import os


print( sys.argv[1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


Domaine1 = mpatches.Patch(color='red', label='Human necesities')
Domaine2 = mpatches.Patch(color='blue', label='Physics')
Domaine3 = mpatches.Patch(color='green', label='Electricity')
plt.legend(handles=[Domaine1,Domaine2,Domaine3])





MOT = sys.argv[1]

type_num = {"abstract":1,"claims":2,"description":3,"documents":4,"total":5}
values_domain = {"A":{"color":'r', "label":"Human necessities"},"G":{"color":'b', "label":"Physics"},"H":{"color":'g', "label":"Electricity"}}

MAIN_DIR = os.getcwd()
os.chdir(MAIN_DIR)

with open('mots.json', 'rU') as json_data:
	cube = json.load(json_data)
json_data.close()


for annee in cube[MOT]:
	for domaine in cube[MOT][annee]:
		for type_name in cube[MOT][annee][domaine]:
			ax.scatter(int(annee), type_num[type_name], cube[MOT][annee][domaine][type_name], c=values_domain[domaine]["color"], marker='o')



ax.set_xlabel('Annee')
ax.set_ylabel('Type')
ax.set_zlabel('Quantite')
plt.title(MOT)




t11 = ['Abstract', 'Claims', 'Description','Documents','Total']




plt.yticks([1,2,3,4,5], t11, size='small')



plt.show()

