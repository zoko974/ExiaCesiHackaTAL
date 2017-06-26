#!/usr/bin/env python

# ATTENTION CE SCRIPT NE S'EXECUTE QU'A PARTIR DU JEU DE DONNEES INITIAL
import os
import re
import platform
import unicodedata
import sys
import copy
import json

MAIN_DIR = os.getcwd()
DATA_DIR = "hasIpcCorr"

#annees = ['2000']
annees = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
domaines = ['A','G','H']
types = ['abstract','claims','description','documents','total']

if (platform.system() == 'Windows'):
	SEP = '\\'
else:
	SEP = '/'

SOUS_CUBE={}

cube = {}

for a in annees:
	SOUS_CUBE[a]={}
	for d in domaines:
		SOUS_CUBE[a][d]={}
		for t in types:
			SOUS_CUBE[a][d][t]=0;

def traiter_fichier(annee, fich):
	global limite
	deja_traite = []
	os.chdir("."+SEP+annee)
	with open(fich, 'rU') as f:
		domaine = 'Z';
  		for line in f:
  			line_splitted = line.split(":::")
  			index = line_splitted[0].strip()
  			if (index == 'ipc'):
  				domaine = line_splitted[1].lstrip()[0]
  				if (domaine not in domaines):
  					continue
  			elif (index in types):
  				if (domaine not in domaines):
  					continue
  				line = unicode(line_splitted[1],'utf-8')
  				line = unicodedata.normalize('NFD', line).encode('ascii', 'ignore')
  				data_tokenized = re.split("[\s\.\,\;\:'\d\(\)\-]+", line)
				for word in data_tokenized:
					if word not in deja_traite:
						deja_traite.append(word)
					if word not in cube:
						cube[word] = copy.deepcopy(SOUS_CUBE)
					cube[word][annee][domaine][index] = cube[word][annee][domaine][index] + 1
					cube[word][annee][domaine]['total'] = cube[word][annee][domaine]['total'] + 1
		for word in deja_traite:
			cube[word][annee][domaine]['documents'] = cube[word][annee][domaine]['documents'] + 1
	os.chdir("..")

os.chdir(MAIN_DIR)
os.chdir(DATA_DIR)
for annee in os.listdir('.'):
	if os.path.isdir("."+SEP+annee):
		for brevet in os.listdir("."+SEP+annee):
			if (brevet[-4:] == ".txt"):
				if(annee in annees):
					traiter_fichier(annee,brevet)
print json.dumps(cube)
