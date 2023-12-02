from cgitb import text
import feedparser as fp
import requests
import os
from bs4 import BeautifulSoup as bs
import json

# Configuration for keywords in a typical ScienceDirect article
SCIENCE_DIRECT_CONFIG = [
    "Follow:",
    "Subscribe:",
    "Date:",
    "Source:",
    "Summary:",
    "Share:",
    "FULL STORY",
    "RELATED TOPICS",
    "RELATED TERMS",
    " Story Source:",
    "RELATED STORIES"
]

# JSON-friendly mapping according to SCIENCE_DIRECT_CONFIG 
SCIENCE_DIRECT_MAPPING = {
    SCIENCE_DIRECT_CONFIG[0]: "follow",
    SCIENCE_DIRECT_CONFIG[1]: "subscribe",
    SCIENCE_DIRECT_CONFIG[2]: "date",
    SCIENCE_DIRECT_CONFIG[3]: "source",
    SCIENCE_DIRECT_CONFIG[4]: "summary",
    SCIENCE_DIRECT_CONFIG[5]: "share",
    SCIENCE_DIRECT_CONFIG[6]: "story",
    SCIENCE_DIRECT_CONFIG[7]: "topics",
    SCIENCE_DIRECT_CONFIG[8]: "terms",
    SCIENCE_DIRECT_CONFIG[9]: "sources",
    SCIENCE_DIRECT_CONFIG[10]: "related"
}


# Article object that abstracts a list of strings containing a representation of an article into a JSON file.
class Article:
    def __init__(self, textlines: list[str], match_keywords: list[str]) -> None:
        match_index = 0
        last_index = -1
        next_index = 0
        self.data = {}
        sections = []
        # Magic code. Targets sections between two match keywords
        # Somehow cannot match for the first section, so I have to manually patch it
        while match_index < len(match_keywords):
            match = match_keywords[match_index]
            index = last_index+1
            while index < len(textlines):
                if textlines[index] == match:
                    next_index = index
                    break
                index += 1
            match_data: list = []
            for i in range(last_index+1, next_index):
                match_data.append(textlines[i])
            last_index = next_index
            sections.append(match_data)
            match_index += 1
        # DEBUG STATEMENT
        #for section in sections:
        #    print(section)
        start = 0
        self.data["title"] = sections[0]
        sections.pop(0)
        while start < len(sections):
            self.data[SCIENCE_DIRECT_MAPPING.get(match_keywords[start])] = sections[start]
            start += 1
        # print(self.data) # FOR DEBUG

    def to_string(self):
        return json.dumps(self.data, indent=4)


def format_html(htmlstr: str):
    htmlstr = htmlstr.strip()
    fmtstr = ""
    index = 0
    while index < len(htmlstr):
        if htmlstr[index] == "\n" and htmlstr[index+1] == "\n": 
            index+=1
            continue
        fmtstr += htmlstr[index]
        index+=1
    return fmtstr


def extract_text_html(entry):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    try:
        response = requests.get(entry.link, headers=headers)
        response.raise_for_status()
        soup = bs(response.text, 'html.parser')
        textlines = format_html(soup.get_text()).splitlines()
        text_title = textlines[0]
        article = Article(textlines, SCIENCE_DIRECT_CONFIG)
        # File handling
        if not os.path.exists("./rss"):
            os.mkdir("./rss")
        # open new file for each new article
        with open(f"./rss/{text_title}.json", "w", encoding="utf-8") as file:
            file.write(article.to_string())
            file.close()
        print(f"Downloading {entry.title}...")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {entry.title}: {e}")
        return None


if __name__ == "__main__":
    print("You are not suppose to run this module individualy")
    rss_feed_url = input("Enter your RSS feed URL: ")
    extract_text_html(rss_feed_url)
                    