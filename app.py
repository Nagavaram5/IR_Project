from flask import Flask, request, jsonify
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from itertools import chain
import string

# Initialize Flask app
app = Flask(__name__)

# Load the indexed data
index = None
with open('index.pkl', 'rb') as f:
    index = pickle.load(f)

# Initialize NLTK resources
wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define an endpoint for query processing
@app.route('/query', methods=['POST'])
def process_query():
    # Get JSON data from the request
    request_data = request.get_json()
    if not request_data or 'query' not in request_data:
        return jsonify({'error': 'Invalid JSON data or missing query field'}), 400
    
    # Process the query
    query = request_data['query']
    processed_query = preprocess_query(query)
    if not processed_query:
        return jsonify({'error': 'Query is empty or contains only stop words'}), 400
    
    # Perform search
    results = index.search(processed_query)
    
    # Return top-K ranked results with cosine similarity scores
    response = [{'doc_id': result[0], 'cosine_similarity': result[1]} for result in results]
    return jsonify({'results': response})

def preprocess_query(query):
    # Tokenize the query
    tokens = word_tokenize(query.lower())
    
    # Remove punctuation and stop words, and lemmatize tokens
    processed_tokens = [wordnet_lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation and token not in stop_words]
    
    # Remove duplicates
    processed_tokens = list(set(processed_tokens))
    
    # Join tokens back into a single string
    processed_query = ' '.join(processed_tokens)
    
    return processed_query

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
