import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import pickle
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def transformation2(self,X):
        
        columns=['id','song_duration_ms', 'acousticness', 'danceability', 'energy',
                'instrumentalness', 'key', 'liveness', 'loudness', 'audio_mode',
                'speechiness', 'tempo', 'time_signature', 'audio_valence']
        X=pd.DataFrame(X,columns=columns)


        #with open(Path('artifacts\data_transformation\encoder.pickle'), 'rb') as f:
        encoder = pickle.loads(open( 'artifacts\data_transformation\encoder.pickle', "rb" ).read())
        #f.close()
        encoder_X=pd.DataFrame(encoder.transform(X[['key','time_signature']]).toarray())
        print(encoder_X.columns)
        X=X.join(encoder_X)
        X.drop(['key','time_signature'],axis=1,inplace=True)

        x =X.values #returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        X_scaled = pd.DataFrame(x_scaled)
        print(X_scaled.shape)
        return X_scaled
    
    def predict(self, data):
        data2=self.transformation2(data)
        prediction = self.model.predict(data2)
        prediction_probabilities=self.model.predict_proba(data2)
        return prediction,prediction_probabilities