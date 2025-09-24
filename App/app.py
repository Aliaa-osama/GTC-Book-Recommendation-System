"""import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommend(title, books, count_matrix, top_n=5):
    try:
        idx = books[books['title'] == title].index[0]
    except IndexError:
        return f"Book '{title}' not found in dataset."

    sim_scores = cosine_similarity(count_matrix[idx], count_matrix).flatten()
    sim_indices = sim_scores.argsort()[-top_n-1:][::-1][1:]
    return books.iloc[sim_indices][['title','average_rating_norm']]


books_list = pickle.load(open('App\model.pkl','rb'))
books = pd.DataFrame(books_list)
books_unique = books.drop_duplicates(subset='title').reset_index(drop=True)
cv = CountVectorizer(max_features=5000, stop_words='english')
count_matrix = cv.fit_transform(books_unique['tags_str'].fillna(''))

st.title('Book Recommender System')

selected_book_name = st.selectbox(
    'which movie do you like',
    books_unique['title'].values
)

if st.button('Recommend'):
    dataframe = recommend(selected_book_name,books_unique,count_matrix,5)
    
    for i, col in enumerate(st.columns(len(dataframe))):
      col.text(dataframe['title'].iloc[i])
      col.text(f"Rating: {dataframe['average_rating_norm'].iloc[i]}")
      #col.image(dataframe['image_url'].iloc[i])
"""

import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Function to get recommendations
def recommend(title, books, count_matrix, top_n=5):
    try:
        idx = books[books['title'] == title].index[0]
    except IndexError:
        return pd.DataFrame()  # return empty dataframe if book not found

    sim_scores = cosine_similarity(count_matrix[idx], count_matrix).flatten()
    sim_indices = sim_scores.argsort()[-top_n-1:][::-1][1:]  # exclude the book itself
    return books.iloc[sim_indices][['title','average_rating_norm']]

# Load model/data
books_list = pickle.load(open(r'App\\model.pkl','rb'))  # raw string for Windows path
books = pd.DataFrame(books_list)
books_unique = books.drop_duplicates(subset='title').reset_index(drop=True)

# Vectorize the tags column
cv = CountVectorizer(max_features=5000, stop_words='english')
count_matrix = cv.fit_transform(books_unique['tags_str'].fillna(''))

# Streamlit UI
st.title('📚 Book Recommender System')

selected_book_name = st.selectbox(
    'Which book do you like?',
    books_unique['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_book_name, books_unique, count_matrix, top_n=5)
    
    if recommendations.empty:
        st.warning(f"Book '{selected_book_name}' not found or no recommendations available.")
    else:
        cols = st.columns(len(recommendations))
        for i, col in enumerate(cols):
            book = recommendations.iloc[i]
            #col.image(book['image_url'] if book['image_url'] else 'https://via.placeholder.com/150', use_column_width=True)
            col.markdown(f"**{book['title']}**")
            col.markdown(f"⭐ {book['average_rating_norm']}")
