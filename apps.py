from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

df=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommendation(song):
    idx=df[df['song']==song].index[0]
    distance=sorted(list(enumerate(similarity[idx])),reverse=True, key=lambda x:x[1])[1:13]
    rec_songs=[]
    for i in distance:
        rec_songs.append(df.iloc[i[0]].song)
    return rec_songs


app=Flask(__name__)
@app.route('/')
def index():
    names=list(df['song'].values)
    return render_template('index.html',name=names)


@app.route('/recommend',methods=['POST'])
def mysong():
    user_song= request.form['names']
    rec_songs=recommendation(user_song)
    return render_template('index.html',songs=rec_songs)


if __name__ == '__main__':
    app.run(debug=True)