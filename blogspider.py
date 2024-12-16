import scrapy

class BlogSpider(scrapy.Spider):
    name = "blog_spider"
    start_urls = ["https://example.com/blog"]

    def parse(self, response):
        for article in response.css('article'):  # Adjust selectors for your target website
            yield {
                'Title': article.css('h2::text').get().strip(),  # Get blog titles
                'Link': article.css('a::attr(href)').get(),      # Get blog links
            }

        # Follow pagination links (if any)
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
