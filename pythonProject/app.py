import streamlit as st
import pickle
import pandas as pd

movies_list=pickle.load(open('movies.pkl','rb'))
movies=movies_list['title'].values()

movies_list=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie,movies_list):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]

    recommend_movies=[]
    for i in movies:
        movie_id=i[0]
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies





st.title('Movie Recommender')

option_selected = st.selectbox('Please select a movie you like :)',movies)

if st.button('Recommend'):
    result=recommend(option_selected,movies_list)
    col1,col2,col3=st.columns(3)
    col4,col5,col6=st.columns(3)
    col7, col8, col9=st.columns(3)
    col10,col11, col12=st.columns(3)
    col13, col14, col15=st.columns(3)
    with col1:
        st.text(result[0])
    with col2:
        st.text(result[1])
    with col3:
        st.text(result[2])
    with col4:
        st.text(result[3])
    with col5:
        st.text(result[4])
    with col6:
        st.text(result[5])
    with col7:
        st.text(result[6])
    with col8:
        st.text(result[7])
    with col9:
        st.text(result[8])
    with col10:
        st.text(result[9])
    with col11:
        st.text(result[10])
    with col12:
        st.text(result[11])
    with col13:
        st.text(result[12])
    with col14:
        st.text(result[13])
    with col15:
        st.text(result[14])