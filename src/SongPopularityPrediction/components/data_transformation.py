import os
from src.SongPopularityPrediction import logger
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from src.SongPopularityPrediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transformation(self,X):
        y=X.pop('song_popularity')
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        imputer = imputer.fit(X)
        X = imputer.transform(X)

        columns=['id', 'song_duration_ms', 'acousticness', 'danceability', 'energy',
                'instrumentalness', 'key', 'liveness', 'loudness', 'audio_mode',
                'speechiness', 'tempo', 'time_signature', 'audio_valence']
        X=pd.DataFrame(X,columns=columns)



        encoder = OneHotEncoder(handle_unknown='ignore')
        encoder_X = pd.DataFrame(encoder.fit_transform(X[['key','time_signature']]).toarray())
        import pickle
        with open(os.path.join(self.config.root_dir,"encoder.pickle"), 'wb') as f:
            pickle.dump(encoder, f)
        f.close()
        X=X.join(encoder_X)
        X.drop(['key','time_signature'],axis=1,inplace=True)

        x =X.values #returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        X_scaled = pd.DataFrame(x_scaled)
        X_scaled['song_popularity']=y
        return X_scaled
    
    def train_test_splitting(self):
        print(self.config.root_dir)
        print(self.config.data_path)
        data = pd.read_csv(self.config.data_path)

        data=self.transformation(data)
        train,test=train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Data tranformation and splitting it into train and test")
        logger.info(train.shape)
        logger.info(test.shape)