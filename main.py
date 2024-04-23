# Importing necessary modules from Scrapy library
import scrapy
from scrapy.crawler import CrawlerProcess

# Defining a custom Spider class for the crawler
class MyCrawler(scrapy.Spider):
    name = "my_crawler"  # Name of the Spider

    # Constructor to initialize Spider attributes
    def __init__(self, seed_url, max_pages, max_depth, *args, **kwargs):
        super(MyCrawler, self).__init__(*args, **kwargs)
        self.start_urls = [seed_url]  # List of URLs to start crawling from
        self.max_pages = max_pages    # Maximum number of pages to crawl
        self.max_depth = max_depth    # Maximum depth to crawl from the seed URL

    # Callback method that parses the response received from each request
    def parse(self, response):
        pass  # Placeholder for parsing logic; actual parsing logic should be implemented here

# Entry point of the program
if __name__ == '__main__':
    # Creating a CrawlerProcess instance with specified settings
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',  # Logging level for the crawler (INFO level)
    })

    # Initiating the crawling process by creating an instance of MyCrawler
    # with specified seed URL, maximum pages, and maximum depth
    process.crawl(MyCrawler, seed_url="https://en.wikipedia.org/wiki/Main_Page", max_pages=10, max_depth=3)
    
    # Starting the crawling process
    process.start()
