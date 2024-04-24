import scrapy
import json
from scrapy.linkextractors import LinkExtractor

class MySpider(scrapy.Spider):
    name = 'myspider'

    # List of seed URLs
    seed_urls = [
        "https://en.wikipedia.org/wiki/Physics",
        "https://en.wikipedia.org/wiki/Chemistry",
        "https://en.wikipedia.org/wiki/Biology",
        "https://en.wikipedia.org/wiki/Astronomy",
        "https://en.wikipedia.org/wiki/Computer_science",
        "https://en.wikipedia.org/wiki/Environmental_science"
    ]
    max_pages = 100
    max_depth = 3
    visited_urls = set()
    data_list = []  # List to store data

    def start_requests(self):
        for url in self.seed_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract content or perform desired actions
        self.visited_urls.add(response.url)
        
        # Extract text content from paragraphs excluding URLs and images
        content = response.xpath('//p//text()').getall()
        content = [text.strip() for text in content if text.strip()]
        
        # Join the extracted text content to form a single string
        content_text = ' '.join(content)
        
        # Limit the amount of scraped text to 1000 words
        content_text = ' '.join(content_text.split()[:1000])

        # Create a dictionary to store data
        data = {
            'title': response.css('title::text').get(),
            'content': content_text
        }
        self.data_list.append(data)  # Append data to the list
    
        # Continue crawling if max pages and max depth are not reached
        if len(self.visited_urls) < self.max_pages:
            depth = response.meta.get('depth', 0)
            if depth < self.max_depth:
                for next_url in self.extract_links(response):
                    yield response.follow(next_url, callback=self.parse, meta={'depth': depth + 1})

    def extract_links(self, response):
        # Extract links from the response
        link_extractor = LinkExtractor(allow_domains=response.url)
        links = link_extractor.extract_links(response)
        return [link.url for link in links]

    def closed(self, reason):
        # Save the data list to output.json at the end
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(self.data_list, f, ensure_ascii=False)
