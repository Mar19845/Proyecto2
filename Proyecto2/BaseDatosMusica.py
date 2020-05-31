import pandas as pd #Dataframe, series
import numpy as np  #Scientfic computing  packgs - arrays

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel


from matplotlib import pyplot as plt
import seaborn as sns

#read csv file with pandas

data = pd.read_csv('base_datos.csv',header=0)



feature_cols = ['Cancion', 'Artista', 'Genero']
X = data[feature_cols] # Features
y = data.Idioma # Target variable

#tfidf = TfidfVectorizer(stop_words='english')
tfidf = TfidfVectorizer("")
tfidf_matrix = tfidf.fit_transform(data['Genero'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data.index, index=data['Cancion']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the songs that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the songs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar songs
    sim_scores = sim_scores[1:11]

    # Get the music
    music_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar songs
    return data['Cancion'].iloc[music_indices]


#print("La cancion que puso es:  Zafar")
#print("se recomineda (?)")
#print(get_recommendations("Zafar"))


#convertir values to a list 
a_list = data['Cancion'].tolist()
for i in a_list:
    print(i)

