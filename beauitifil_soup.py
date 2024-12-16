import requests
from bs4 import BeautifulSoup
import csv

URL = "https://example.com/blog"

response = requests.get(URL)

if response.status_code == 200:
    print("Successfully accessed the website!")
else:
    print("Failed to access the website. Status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

blog_posts = []
for article in soup.find_all('article'): 
    title = article.find('h2').text.strip()  
    link = article.find('a')['href']
    blog_posts.append({'Title': title, 'Link': link})

output_file = "blog_posts.csv"

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
    writer.writeheader()
    writer.writerows(blog_posts)

print(f"Scraped data saved successfully to {output_file}.")
