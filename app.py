import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def main():
    activities=['About','Movie Recommendation Engine','Developer']
    option=st.sidebar.selectbox('Menu Bar:',activities)
    if option=='About':
        html_temp = """
        <div style = "background-color: yellow; padding: 10px;">
            <center><h1>ABOUT PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.write('Have you ever been on an online streaming platform like Netflix, Amazon Prime, Voot? I watched a movie and after some time, that platform started recommending me different movies and TV shows. I wondered, how the movie streaming platform could suggest me content that appealed to me. Then I came across something known as Recommendation System. This system is capable of learning my watching patterns and providing me with relevant suggestions. Having witnessed the fourth industrial revolution where Artificial Intelligence and other technologies are dominating the market, I am sure that you must have come across a recommendation system in your everyday life.')
        st.subheader('Movie Recommendation System Project using ML')
        image=Image.open('1.jpg')
        st.image(image,use_column_width=True)
        st.write('The main goal of this machine learning project is to build a recommendation engine that recommends movies to users. This ML project is designed to help us understand the functioning of how a recommendation system works. In this I have developed an Content-Based Filter. ')
        
        st.subheader('So, What is a Recommendation System?')
        st.write('A recommendation system provides suggestions to the users through a filtering process that is based on user preferences and browsing history. The information about the user is taken as an input. The information is taken from the input that is in the form of browsing data. This information reflects the prior usage of the product as well as the assigned ratings. A recommendation system is a platform that provides its users with various contents based on their preferences and likings. A recommendation system takes the information about the user as an input. The recommendation system is an implementation of the machine learning algorithms.')
        image=Image.open('2.png')
        st.image(image,use_column_width=True)
        st.write('A recommendation system also finds a similarity between the different products. For example, Netflix Recommendation System provides you with the recommendations of the movies that are similar to the ones that have been watched in the past. Furthermore, there is a collaborative content filtering that provides you with the recommendations in respect with the other users who might have a similar viewing history or preferences. There are two types of recommendation systems – Content-Based Recommendation System and Collaborative Filtering Recommendation')


    elif option=='Movie Recommendation Engine':
        html_temp = """
        <div style = "background-color: SKYBLUE; padding: 10px;">
            <center><h1>Movie Recommendation Engine</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        
        #helper functions(use them when needed)
        def get_title_from_index(index):
            return df[df.index==index]["title"].values[0]

        def get_index_from_title(title):
            return df[df.title==title]["index"].values[0]

        #Read CSV file
        df=pd.read_csv("movie_dataset.csv")

        #Select Features
        features=['keywords','cast','genres','director']

        
        for feature in features:
            df[feature]=df[feature].fillna('')

        # Create a column in the dataframe that combines all the features
        def combine_features(row):
            try:
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            except:
                print("Error",row)
        df["combined_features"]=df.apply(combine_features,axis=1)
        
        
        #Create count matrix from this new combined column
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(df["combined_features"])

        #Compute the cosine similarity based on the  count_matrix
        cosine_sim=cosine_similarity(count_matrix)
        st.header('Please Enter The Name of the Movie')
        movie_user_likes=st.text_input("input text")


        #get the index of this movie from its title
        movie_index=get_index_from_title(movie_user_likes)
        
        similar_movies=list(enumerate(cosine_sim[movie_index]))

        #get a list of similar movies in descending order of similarity score
        sorted_similar_movies=sorted(similar_movies,key= lambda x:x[1],reverse=True)

        #print the titles of first 50 movies
        st.subheader('The top 50 movies suggested for you are:-')
        i=0
        for movie in sorted_similar_movies:
            st.write(get_title_from_index(movie[0]))
            i=i+1
            if i>50:
                break


        
    
    elif option=='Developer':
        st.balloons()
        st.title('Prepared by:-')
        st.header('SAURAV BORAH :sunglasses:')
        st.subheader('Source code:-')
        st.write('https://github.com/SAURAVBORAH22/Movie-Recommendation-Engine')
        st.subheader('My LinkedIn profile:-')
        st.write('https://www.linkedin.com/in/saurav-borah-a7751818b/')
        




            
if __name__ == '__main__':
    main()