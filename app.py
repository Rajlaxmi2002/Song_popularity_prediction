from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import math
from src.SongPopularityPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

is_trained=False

@app.route('/',methods=['GET'])
def home():
    print("homepage")
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    if request.method == 'POST':
        # try:
            #  reading the inputs given by the user
            data=[]
            id=float(request.form['id'])    
            song_duration_ms=float(  request.form['song_duration_ms'])
            acousticness=float(request.form['acousticness'])  
            
            danceability=float(request.form['danceability'])  
            
            energy=float(request.form['energy'])  
            
            instrumentalness=float(request.form['instrumentalness'])  
            
            key=float(request.form['key'])  
            
            liveness=float(request.form['liveness'])  
            
            loudness=float(request.form['loudness'])  
            
            audio_modes=float(request.form['audio_modes'])    
            
            speechiness=float(request.form['speechiness'])  
            
            tempo=float(request.form['tempo'])  
            
            time_signature=float(request.form['time_signature'])    
            
            audio_valence=float(request.form['audio_valence'])  
              
       
         
            data = [id,song_duration_ms,acousticness,danceability,energy,instrumentalness,key,liveness,loudness,audio_modes,speechiness,tempo,time_signature,audio_valence]
             
            data = np.array(data).reshape(1, 14)
            path="artifacts\model_trainer\model.joblib"
            if os.path.isfile(path)==False:
                os.system("python main.py")
                is_trained=True
            obj = PredictionPipeline()
            
            predict,prediction_probabilities = obj.predict(data)    
            probability=prediction_probabilities[0]
            #print(prediction_probabilities)
            if(predict==0):
                 prob=probability[0]
                 prob=math.ceil(prob*10000)
                 prob=prob/100
                 predict="not popular with probability of "+str(prob)+"%."
            else:
                 prob=probability[1]
                 prob=math.ceil(prob*10000)
                 prob=prob/100
                 predict="popular with probability of "+str(prob)+"%."
            return render_template('results.html', prediction = str(predict))

        # except Exception as e:
        #     print('The Exception message is: ',e)
        #     return 'something is wrong'

    else:
        return render_template('index.html')
    

if __name__== "__main__":
    print("starting app")
    app.run(host="0.0.0.0",port= 8080,debug=True)