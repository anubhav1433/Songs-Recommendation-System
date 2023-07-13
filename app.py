import streamlit as st 
import pickle
import pandas as pd

def recommend(song):
    idx= songs[songs['song']==song].index[0]
    distance=sorted(list(enumerate(similarity[idx])),reverse=True, key=lambda x:x[1])[1:11]
    
    rec_songs=[]
    for i in distance:
        rec_song=songs.iloc[i[0]].song
        rec_artist=songs.iloc[i[0]].artist
        rec_songs.append((rec_song,rec_artist))
    return rec_songs

song_list=pickle.load(open('df.pkl','rb'))
songs=pd.DataFrame(song_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Song Recommendor System')
st.sidebar.title('Please select a song')

selected_song=st.sidebar.selectbox('Select a song',songs['song'].values)

if st.sidebar.button('Recommend'):
    recommendations=recommend(selected_song)
    st.title('Here are your recommended songs:')
    for song,artist in recommendations:
        st.write(song+" by "+artist)