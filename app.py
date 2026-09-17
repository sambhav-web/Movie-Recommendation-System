import streamlit as st
import pickle
import joblib
st.title('Movie Recommendation System')
with open('movies.pkl','rb') as file:
    data=pickle.load(file)
similarities=joblib.load('similarity.joblib')
def recommend(movie):
    final_movies=[]
    movie_index=data[data['title']==movie].index[0]
    recommendations=similarities[movie_index]
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    movie_indexes=[i for i,j in movie_list]
    for i in movie_indexes:
        final_movies.append(data[data.index==i]['title'].values[0])
    return final_movies

movie=st.selectbox(label='Choose a movie : ',options=[None]+list(data['title'].values))
if st.button('Recommend') and movie:
    st.subheader(f'Your selected movie : {movie}')
    st.success('The recommended movies are : ')
    recommended_movies=recommend(movie)
    for movie in recommended_movies:
        st.write(movie)