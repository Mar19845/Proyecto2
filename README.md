# Proyecto2
Sistema de recomendacion musical

## Overview
Este código pertenece a un sistema de recomendacion musical. El sistema se fija en aspectos como el género y el idioma para
lograr un filtrado exitoso en las recomendaciones.

## Base de datos
El archivo base_datos.csv contiene una base de datos con canciones, sus artistas, el género de cada una, el disco,
la duracion y el año en que cada cancion fue lanzada.

## Contacto con la base de datos
El archivo ClaseBaseDeDatosMusica.py contiene las funciones para poder leer el archivo base_datos.csv y de esta manera 
efectuar las operaciones tales como recomendar, mostrar y eliminar cancion.
```
class BaseMusica:
    ***
    data = pd.read_csv('base_datos.csv',header=0)
    ***
    def RecomendarCancion(self,title, cosine_sim=cosine_sim)
    def MostrarInfo(self)
    def EliminarCancion(self)
    
```

## Aspectos Relevantes para el funcionamiento del sistema
### Dependencias necesarias para el funcionamiento del programa
pandas, sklearn, numpy, matplotlib, seaborn, neo4j, networkx

### Clase base de datos
Dentro del archivo ClaseBaseDeDatosMusica.py leer el archivo .csv con pandas
```
class BaseMusica:
    data = pd.read_csv('base_datos.csv',header=0)
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(data['Genero'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(data.index, index=data['Cancion']).drop_duplicates()
    
```
### Para cargar el programa es necesario importar los siguientes paquetes
Dentro del archivo ClaseBaseDeDatosMusica.py
```
import pandas as pd 
import numpy as np  

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from matplotlib import pyplot as plt
import seaborn as sns
    
```
Dentro del archivo Grafo.py
```
import networkx as nx
import matplotlib.pyplot as plt
    
```
Dentro del archivo BaseDeDatosMusica.py
```
import pandas as pd #Dataframe, series
import numpy as np  #Scientfic computing  packgs - arrays
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from matplotlib import pyplot as plt
import seaborn as sns
    
```
Dentro del archivo BaseDeDatosMusica.py
```
import pandas as pd #Dataframe, series
import numpy as np  #Scientfic computing  packgs - arrays
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from matplotlib import pyplot as plt
import seaborn as sns
    
```
## Uso
Para utilizar el programa se debe leer y compilar el archivo Main.py y tener todos los archivos en la misma carpeta
