import json
from ebooklib import epub


def fetch_json_text(filename):
    with open(f"./rss/{filename}.json", "r") as file:
        json_data = json.load(file)
    print("JSON obejects: ", type(json_data))
    
    article_title = json_data["title"][0]
    publish_date = json_data["date"][0]
    article_source = json_data["source"][0]
    article_summary = json_data["summary"][0]
    article_main = ''
    for i in json_data["story"]:
        article_main = article_main + i
    article_sources = ''
    for i in json_data["sources"]:
        article_sources = article_sources + "\n" + i
    
    ''' debug
    print(article_sources)
    print(article_main)    
    print(article_summary)
    print(article_title)
    '''

def create_epub(title, date, source, main, sources):
    book = epub.EpubBook()

    book.set_identifier("1145141919810")
    book.set_title(title)
    book.set_language('en')
    book.add_author(source)
    # not done yet...
