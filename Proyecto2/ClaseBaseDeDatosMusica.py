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



class BaseMusica:
    data = pd.read_csv('base_datos.csv',header=0)
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(data['Genero'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(data.index, index=data['Cancion']).drop_duplicates()
    
    print("se creo la clase paper")
    
    def RecomendarCancion(self,title, cosine_sim=cosine_sim):
        # Get the index of the songs that matches the title
        idx = self.indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the music
        music_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar songs
        return self.data['Cancion'].iloc[music_indices]
    
#x = BaseMusica()
#print(x.RecomendarCancion("Zafar"))