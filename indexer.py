# Importing necessary modules from scikit-learn library
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Function to build an index for the given documents
def build_index(documents):
    # Initializing a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Transforming the documents into TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Computing cosine similarity between TF-IDF vectors to get similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Saving the vectorizer and similarity matrix to a file using pickle
    with open('index.pickle', 'wb') as handle:
        pickle.dump((vectorizer, similarity_matrix), handle, protocol=pickle.HIGHEST_PROTOCOL)

# Entry point of the program
if __name__ == '__main__':
    # Example documents
    documents = ["This is document 1", "Another document", "Yet another document"]
    
    # Building the index for the given documents
    build_index(documents)
