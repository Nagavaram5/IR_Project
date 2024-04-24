import os
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize

class Indexer:
    def __init__(self):
        self.index = {}
        self.vectorizer = TfidfVectorizer(min_df=1, stop_words=None)  # Set stop_words to None
        nltk.download('punkt')  # Download the punkt tokenizer if not already downloaded

    def build_index_from_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        self.build_index(documents)

    def build_index(self, documents):
        # Ensure that the documents contain 'content' field
        contents = [doc['content'] for doc in documents if 'content' in doc]
        tokenized_contents = [' '.join(word_tokenize(content)) for content in contents]
        tfidf_matrix = self.vectorizer.fit_transform(tokenized_contents)
        for idx, row in enumerate(tfidf_matrix):
            self.index[idx] = row

    def save_index(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.index, f)

    def load_index(self, filename):
        with open(filename, 'rb') as f:
            self.index = pickle.load(f)

    def search(self, query, top_n=5):
        query_vector = self.vectorizer.transform([query])
        scores = {}
        for doc_id, doc_vector in self.index.items():
            similarity = cosine_similarity(query_vector, doc_vector)
            scores[doc_id] = similarity[0][0]
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:top_n]

if __name__ == "__main__":
    indexer = Indexer()
    json_file = 'output.json'
    indexer.build_index_from_json(json_file)
    indexer.save_index('index.pkl')
    indexer.load_index('index.pkl')
