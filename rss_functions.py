import feedparser as fp
import requests
import re
from bs4 import BeautifulSoup as bs

def extract_text_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        news_feed = fp.parse(url)
        for entry in news_feed.entries:
            response = requests.get(entry.link, headers=headers)
            response.raise_for_status()

            soup = bs(response.text, 'html.parser')
            text = soup.get_text()
        
        filename = news_feed.feed.title # writing all the articles in to one html file

        '''
            filename = entry.title 

            with open(f"{filename}.html", "w", encoding="utf-8") as file:
                file.write(text)
            print(f"Downloading {entry.title}...") # write each article into individual html file
            # not sure which one to use
        '''


        with open(f"{filename}.html", "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Downloading {entry.title}...")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

if __name__ == "__main__":
    print("You are not suppose to run this module individualy")
    rss_feed_url = input("Enter your RSS feed URL: ")
    extract_text_html(rss_feed_url)
                    