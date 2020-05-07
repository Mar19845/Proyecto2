import pandas as pd #Dataframe, series
import numpy as np  #Scientfic computing  packgs - arrays

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns
#%matplotlib inline

#data = pd.read_csv("base_datos.csv",names=["Track","Artist","Album","Duration","Genero","Year","Id","Idioma"],header=0)
data = pd.read_csv('base_datos.csv')
#type(data[''])
print(data.head())
songsEsp = data[data["Idioma"]== "Espanol"]
songs= data["Cancion"]
#print(songs)
lista = []
#for i in songs:
#    lista.append(i)
#for x in lista:
#    print(x)
