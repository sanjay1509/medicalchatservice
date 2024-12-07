
import time
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score



def Testing( model, file):
	
	test_ = pd.read_csv(file)
	Y=test_['Disease']
	p_model = pickle.load(open(model, 'rb'))
	predicted_class = p_model.predict(test_['Sym'])
	accuracy = model_assessment(Y, predicted_class)
	return accuracy

def model_assessment(y_test, predicted_class):
	accuracy = accuracy_score(y_test, predicted_class)
	precision=(precision_score(y_test, predicted_class,  average='micro', pos_label='Allergy'))
	recall=(recall_score(y_test, predicted_class,  average='micro',pos_label='Allergy'))
	fscore=(f1_score(y_test, predicted_class,  average='micro',pos_label='Allergy'))
	return(accuracy,precision,recall,fscore)


if __name__ == '__main__':
	Testing('svm.sav','Testset.csv')
