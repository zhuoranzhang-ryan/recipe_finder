import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read recipe_final.txt
df_words = pd.read_csv("recipe_final.txt", index_col=[0])

# Map the combined word column into an array
text = df_words['combined words'].to_list()

# Calculate the TF-IDF matrix
model = TfidfVectorizer()
matrix = model.fit_transform(text)

# define a function to preprocess the search query:
def query_preprocessing(query):

    query = re.sub('[^a-zA-Z]', ' ', query)
    query = query.split()
    ps = PorterStemmer()
    query = [ps.stem(word) for word in query if not word in set(stopwords.words('english'))]
    query = ' '.join(query)
    
    return query

# define a function to return the best three recipes
def get_selection_top3(query):
    
    query = query_preprocessing(query)
    query_matrix = model.transform([query])
    similarity = cosine_similarity(matrix, query_matrix)
    
    similarity.flatten()
    top5k = np.argsort(similarity.flatten())[::-1][:50]
    top5ksorted = np.sort(similarity.flatten())[::-1][:50]
    length = len(top5k)
    results = []
    
    for i in range(length):
        j = top5k[i]
        rating = df_words.loc[j]['rating']
        review = df_words.loc[j]['review']
        tmp = top5ksorted[i] * rating * review
        results.append(tmp)
        
    resultssorted = np.argsort(results)
    
    top3 = []
    
    for i in range(3):
        bestindex = top5k[resultssorted[-(i+1)]]
        top3.append(df_words.loc[bestindex]['id'])
    
    return top3

