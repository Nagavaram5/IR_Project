# Information Retrieval Final Project

## Nagavaram Saiteja
## Hawk Id: A20552041

## Abstract
This project encompasses a comprehensive web document retrieval system, including web crawling, search indexing, and query processing. The system uses Scrapy for web crawling, Scikit-Learn for building an inverted index, and Flask for serving query results. The objective was to create a flexible, extensible system capable of crawling web content, indexing it for efficient search, and providing top-ranked search results. The project achieved its goals, demonstrating the ability to crawl websites, build search indexes, and handle search queries. Future work could

## Overview
The solution involves three key components: a Scrapy-based crawler, a Scikit-Learn-based indexer, and a Flask-based query processor. The crawler is responsible for gathering web content based on configurable parameters such as seed URL, max pages, and max depth. The indexer processes the collected data to build an inverted index using TF-IDF and cosine similarity for query matching. The query processor provides an HTTP endpoint for users to submit search queries and returns top-ranked results in JSON format. This system aligns with contemporary approaches to web scraping and information retrieval.

### Relevant Literature
Relevant literature for this project includes:
- Information Retrieval: Works by Manning, Raghavan, and Schütze on information retrieval and search engines.
- Web Scraping: Books and articles on best practices and ethical considerations in web scraping.
- Natural Language Processing: Publications on text analysis and search techniques, such as cosine similarity and TF-IDF.

### Proposed System
The proposed system is designed to be modular and flexible, allowing for future extensions. It uses open-source technologies for web crawling, search indexing, and query processing. The use of Scrapy for web crawling provides robust tools for gathering data from websites. Scikit-Learn's TF-IDF-based indexing allows for efficient search and retrieval, while Flask's simplicity enables easy creation of a query endpoint.

## Design
The system's design comprises three main parts:

1. **Web Crawler**: A Scrapy-based crawler that collects web documents in HTML format. It can be initialized with a seed URL, a limit on the number of pages to crawl, and a maximum depth.

2. **Search Indexer**: A Scikit-Learn-based indexer that builds an inverted index using TF-IDF for vectorization. It also calculates cosine similarity for matching search queries with indexed documents.

3. **Query Processor**: A Flask-based processor that accepts search queries via HTTP POST requests and returns top-ranked results. It includes query validation to ensure correct input format.

These components interact to provide a complete web document retrieval and search system. The modular design allows for future improvements and extensions, such as distributed crawling, vector embeddings, or advanced query processing techniques.

## Architecture
The system architecture consists of software components, interfaces, and implementation details:

### Software Components
- **Web Crawler (Scrapy)**: Collects web content and outputs to JSON or CSV.
- **Search Indexer (Scikit-Learn)**: Builds a TF-IDF-based inverted index and supports search operations.
- **Query Processor (Flask)**: Processes HTTP POST requests, validates queries, and returns search results.

### Interfaces
- **Scrapy**: The crawler outputs web documents in a structured format, which can be used by the indexer.
- **Scikit-Learn**: The indexer constructs an inverted index and exposes methods for searching.
- **Flask**: The processor provides an HTTP endpoint for search queries and returns results in JSON format.

### Implementation
- **Web Crawler**: The crawler uses Scrapy's built-in capabilities to manage crawling limits and depth, with optional support for distributed crawling (Scrapyd).
- **Search Indexer**: The indexer uses Scikit-Learn's `TfidfVectorizer` for vectorization and cosine similarity for search. It also supports saving and loading the index with pickle.
- **Query Processor**: The processor uses Flask to create a simple HTTP endpoint. It includes query validation and error handling to ensure valid requests.

## Operation
To operate the system, follow these steps:

- **Web Crawler**:
   - Run the Scrapy-based web crawler with specific arguments for start URL, max pages, and max depth.
   - Use the command: 
     ```bash
     scrapy crawl web_spider -a start_url='http://example.com' -a max_pages=10 -a max_depth=2
     ```

- **Search Indexer**:
   - Load documents (e.g., from crawler output) and build the inverted index using Scikit-Learn's TF-IDF vectorization.
   - Save the index to a pickle file for persistence.
   - Search for queries using the indexer's search method, specifying the query and number of top results to return.

- **Query Processor**:
   - Start the Flask server with:
     ```bash
     flask run
     ```
   - Send HTTP POST requests to the `/search` endpoint with JSON data containing the search query and optional `top_k` parameter to get top-ranked search results.

## Conclusion

### Summary of Results
The project successfully met its objectives by building a system capable of web crawling, indexing, and query processing. The web crawler collected web documents within specified constraints, the indexer constructed a usable inverted index, and the Flask-based query processor effectively handled search queries, returning accurate top-ranked results.

### Project Success/Failure
The project was successful. Factors contributing to its success included a robust design, the use of well-chosen technologies, and effective implementation. The modular structure allowed for flexibility and adaptability, contributing to the system's overall stability and reliability.

### Challenges and Limitations
Several challenges were encountered during the project, such as ensuring compliance with robots.txt rules and handling diverse web structures. There were also some limitations, including scalability issues and potential non-compliance with certain website terms of use. The system's handling of complex queries could be improved in future iterations.

### Outputs and Deliverables
The project produced several significant outputs and deliverables, including:
- A functional web crawler that outputs collected web documents.
- A Scikit-Learn-based inverted index built with TF-IDF.
- A Flask-based query processor providing an HTTP endpoint for search queries.
These deliverables demonstrate the complete operation of the system from crawling to query processing.

### Caveats/Cautions
Users of this system should be aware of potential compliance issues with website terms of use and robots.txt rules. There could also be security or privacy concerns when dealing with sensitive data. Additionally, the system's scalability might be limited for large-scale web crawling projects.

### Future Work and Recommendations
Future work could focus on improving the scalability of the web crawler, exploring distributed crawling options, and integrating more advanced indexing techniques like word embeddings. Other recommendations include enhancing query processing with NLP tools and implementing additional security measures to address potential privacy concerns.


## Data Sources
Wikimedia Foundation. (2024, March 7). Main page. Wikipedia. [https://en.wikipedia.org/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page)

Welcome to Flask - Flask Documentation (3.0.x). (n.d.). [Welcome to Flask](https://flask.palletsprojects.com/en/3.0.x/)

NiceGUI. (n.d.). [NiceGUI](https://nicegui.io/)

Scikit-Learn. (n.d.). [Learn](https://scikit-learn.org/stable/)

Scrapy 2.11 documentation - Scrapy 2.11.1 documentation. (2024, April 11). [Scrapy 2.11 documentation](https://docs.scrapy.org/en/latest/)

## Source Code
The source code for this project consists of the following key files:

### main.py
![WhatsApp Image 2024-04-22 at 11 06 13 PM](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/1815b8dc-6b73-4f71-8f84-c71d625aa4f0)

![WhatsApp Image 2024-04-22 at 11 06 13 PM (1)](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/9073dc9a-acc3-46f9-9561-5f2b7bb445fa)


### indexer.py
![WhatsApp Image 2024-04-22 at 11 07 18 PM](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/dd2ff78b-2f58-4ff4-bb16-1ae6aed1ab19)

![WhatsApp Image 2024-04-22 at 11 07 18 PM (1)](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/c362619a-ee7d-49d1-bd8a-73d4920503fb)

![WhatsApp Image 2024-04-22 at 11 07 18 PM (2)](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/b4c28e8a-5f2c-437b-89d1-b7ba3d951d01)

### indexer2.py
![WhatsApp Image 2024-04-22 at 11 08 34 PM](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/768ddb3b-81d2-4815-ab08-451ec17eb634)

![WhatsApp Image 2024-04-22 at 11 08 35 PM](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/de152942-a54c-458f-82bf-7c22009ad003)

![WhatsApp Image 2024-04-22 at 11 08 35 PM (1)](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/e7e44820-d78b-4b59-848b-98f243324e66)

![WhatsApp Image 2024-04-22 at 11 08 35 PM (2)](https://github.com/Nagavaram5/IR_FinalProject/assets/72292611/a4deed1c-40e6-41fd-8a7c-1c404c0f6aae)

### Dependencies
The project uses the following open-source dependencies:

- **Python 3.10+**: Base programming language.
- **Scrapy 2.11+**: Web crawling framework.
- **Scikit-Learn 1.2+**: Machine learning library for TF-IDF and cosine similarity.
- **Flask 2.2+**: Web framework for HTTP endpoint.
- **NLTK**: Natural Language Toolkit, for potential use in query processing.
- **Scrapyd**: Optional distributed crawling support.

## Bibliography
The following references are cited for relevant literature and best practices:

1. Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. _Introduction to Information Retrieval_. New York: Cambridge University Press, 2008.

2. Fielding, Roy T., and Richard N. Taylor. "Architectural Styles and the Design of Network-Based Software Architectures." _ACM Transactions on Software Engineering and Methodology_ 2, no. 2 (1997): 115-143.

3. Bird, Steven, Ewan Klein, and Edward Loper. _Natural Language Processing with Python_. Beijing: O'Reilly Media, 2009.

4. Scrapy Documentation. "Scrapy." [Scrapy Documentation](https://docs.scrapy.org/en/latest/) (accessed April 22, 2024).

5. Scikit-Learn Documentation. "Scikit-Learn." [Scikit-Learn Documentation](https://scikit-learn.org/stable/) (accessed April 22, 2024).

6. Flask Documentation. "Flask." [Flask Documentation](https://flask.palletsprojects.com/en/latest/) (accessed April 22, 2024).

7. NiceGUI. (n.d.). [NiceGUI](https://nicegui.io/)



