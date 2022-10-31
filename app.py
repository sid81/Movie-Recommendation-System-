import pickle
from urllib import response
import requests
import streamlit as st
import pandas as pd

st.title("Recomended Movie list Sytem:")
base="dark"
primaryColor="purple"

#creating fun to get image using api
def get_image(id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=42ebf6486ad38dd6a3356ed84aa2f20a&language=en-US'.format(id))
   data=response.json()
   x=data['poster_path']
   return 'https://image.tmdb.org/t/p/w300/'+ x


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=distance[movie_index]
    recommended_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:8]
    recommended_movie=[]
    #for image fetch
    recommended_movie_image=[]
    
    
    for i in recommended_list:
        id=movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
    
        recommended_movie_image.append(get_image(id))
        
    return recommended_movie,recommended_movie_image



movies_dict=pickle.load(open('imd_recommend.pkl','rb'))
movies=pd.DataFrame(movies_dict)

distance=pickle.load(open('where magic happens.pkl','rb'))

option=st.selectbox(
    'Enter the movie name?', movies['title'])

if st.button('Recommend'):
    recom,images=recommend(option)
    #for i in recom:
    #   st.write(i)
    col1, col2, col3, col4, col5, col6,col7 = st.columns(7)
    with col1:
        st.text(recom[0])
        st.image(images[0])
    with col2:
        st.text(recom[1])
        st.image(images[1])

    with col3:
        st.text(recom[2])
        st.image(images[2])
    with col4:
        st.text(recom[3])
        st.image(images[3])
    with col5:
        st.text(recom[4])
        st.image(images[4])
    with col6:
        st.text(recom[5])
        st.image(images[5])
    with col7:
        st.text(recom[6])
        st.image(images[6])