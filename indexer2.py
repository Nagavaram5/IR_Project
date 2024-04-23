# Importing necessary modules from Flask
from flask import Flask, request, jsonify

# Creating a Flask application instance
app = Flask(__name__)

# Define a route for processing queries
@app.route('/query', methods=['POST'])
def process_query():
    # Extracting the query from the JSON data received in the request
    query = request.json.get('query')
   
    # Dummy results (to be replaced with actual logic)
    results = [{"document": "Document 1", "score": 0.85}, {"document": "Document 2", "score": 0.75}]
    
    # Returning the results as JSON
    return jsonify(results)

# Entry point of the program
if __name__ == '__main__':
    # Running the Flask application in debug mode
    app.run(debug=True)
