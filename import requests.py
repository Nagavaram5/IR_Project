import requests

# Define the URL of your Flask app
url = 'http://127.0.0.1:5000/query'  # Replace with the actual URL if deployed elsewhere

# Define the query data
query_data = {'query': 'science and technology'}

# Make a POST request to the /query endpoint
response = requests.post(url, json=query_data)

# Print the response
print(response.json())
