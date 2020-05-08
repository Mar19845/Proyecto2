class EnsembleClasifier():

    def __init__(self,base_classifier,labels):
        self.classifier = [base_classifier]
        self.labels = labels
    def add_classifier(self,classifier):
        self.classifier.append(classifier)
    def remove_last_classifier(self):
        self.classifier.pop(-1)
    def predict_proba(self,X):
        return np.array([clf.predict_proba(X) for clf in self.classifier]).sum(axis=0)/len(self.classifier)
    def predict(self,X):
        return labels[np.argmax(self.predict_proba(X),axis=1)]
    def error(self,X,y):
        return 1 - accuracy_score(y,ensembleClasifier.predict(X))

class Artificial_data():

    def __init__(self,X,y,dtypes):
        self.dtypes = {}
        self._generator = {}
        self.labels = y.unique()
        for c,dtype in zip(X.columns,dtypes):
            self.dtypes[c] = dtype
            if dtype == 'numeric':
                self._generator[c] = {'mean':X[c].mean(),'std':X[c].std()}
            else:
                unique_values = X[c].value_counts() / X.shape[0]
                self._generator[c] = {'values':unique_values.index,'prob':unique_values.values}

    def sample_generator(self,ensembleClasifier,nb_samples=1):
        syn_X = pd.DataFrame()
        for c in self.dtypes.keys():
            if self.dtypes[c] == 'numeric':
                syn_X[c] = np.random.normal(self._generator[c]['mean'],self._generator[c]['std'],nb_samples)
            else:
                syn_X[c] = np.random.choice(self._generator[c]['values'],p=self._generator[c]['prob'],
                                             size=nb_samples,replace=True)
        p_hat = ensembleClasifier.predict_proba(syn_X)
        p_hat[p_hat==0] = 1e-5
        inverse_p = 1/p_hat
        new_p = inverse_p / inverse_p.sum(axis=1)[:, np.newaxis]
        syn_y = [np.random.choice(self.labels,p=new_p[i]) for i in range(nb_samples)]
        return syn_X,syn_y  


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train_base, X_test, y_train_base, y_test = train_test_split( pd.DataFrame(X), pd.Series(y), 
                                                              test_size = 0.3, random_state = 100)

# dtypes=['numeric' for _ in range(7)] + ['nominal'] #use this for abalone dataset
dtypes=['numeric' for _ in range(4)]
np.random.seed(1)
artifical_data = Artificial_data(X_train_base,y_train_base,dtypes)

c_size = 15
i_max = 300 
R_size = len(X_train_base)
i = 1
trails =1
labels = np.unique(y_train_base)
clf_entropy = DecisionTreeClassifier(random_state = 1, max_depth=2)
clf_entropy.fit(X_train_base, y_train_base)


ensembleClasifier = EnsembleClasifier(clf_entropy,labels)
error_bst = ensembleClasifier.error(X_train_base,y_train_base)

while (i<c_size and trails<i_max):
    X_syn,y_syn =artifical_data.sample_generator(ensembleClasifier,R_size)
    X_train=pd.concat([X_train_base,X_syn],axis=0)
    y_train=np.append(y_train_base,y_syn,axis=0)

    C_prime=DecisionTreeClassifier( random_state = 1, max_depth=2)
    C_prime.fit(X_train, y_train)

    ensembleClasifier.add_classifier(C_prime)

    error_i = ensembleClasifier.error(X_train_base,y_train_base)

    if error_i <= error_bst:
        print('improvement')
        error_bst = error_i
        print(error_i)
        i += 1
    else:
        ensembleClasifier.remove_last_classifier()

    trails +=1