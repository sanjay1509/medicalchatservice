
import sys
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline


class Training:

    def train(algo):
        alg=None

        if algo=='nb':
            alg=BernoulliNB()
        

        if algo=='nn':
            alg=MLPClassifier()
        

        if algo=='svm':
            alg=svm.SVC()
        
        if algo=='rf':
            alg=RandomForestClassifier()
        


        train_file="Symptoms2.csv"
        df = pd.read_csv(train_file)
        df=df.drop_duplicates()

        
        tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
        pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', alg)])
        filename = str(algo)+'.sav'
        pickle.dump(pipeline.fit(df['Sym'], df['Disease']), open(filename, 'wb'))

    


if __name__ == "__main__":
    Training.train('nn')
    Training.train('svm')
    Training.train('nb')
    Training.train('rf')

