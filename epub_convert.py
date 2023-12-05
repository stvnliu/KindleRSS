import json
from ebooklib import epub
from colorama import Back, Fore

def fetch_json_text(filename):
    with open(f"./rss/{filename}.json", "r") as file:
        json_data = json.load(file)
    print("JSON objects: ", type(json_data))
    
    article_title = json_data["title"][0]
    publish_date = json_data["date"][0]
    article_source = json_data["source"][0]
    article_summary = json_data["summary"][0]
    article_main = '\n'.join(json_data["story"])
    article_sources = '\n'.join(json_data["sources"])

    # create_epub(article_title, publish_date, article_source, article_main, article_sources, filename)
    
    '''debug
    print(article_title)
    print(publish_date)
    print(article_summary)
    print(article_main) 
    print(article_sources)   
    '''

    return article_title, publish_date, article_source, article_main, article_sources


def create_epub(title, date, source, main, sources, file_name):
    book = epub.EpubBook()

    book.set_identifier("1145141919810")
    book.set_title(title)
    book.set_language('en')
    book.add_author(source)

    # Initialize Table of Contents (TOC) and spine
    toc = []
    spine = ['nav']

    # Create main content item (EpubHtml)
    main_item = epub.EpubHtml(title=title, file_name="main.xhtml", content=main)
    book.add_item(main_item)

    # Add main content to TOC and spine
    toc.append(epub.Link("main.xhtml", title, title))
    spine.append(main_item)

    # Define TOC
    book.toc = tuple(toc)

    # Add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define CSS style
    style = 'pre{white-space:pre-wrap;background:#f7f9fa;padding:10px 15px;color:#263238;line-height:1.6;font-size:13px;border-radius:3px;margin-top:0;margin-bottom:1em;overflow:auto}b,strong{font-weight:bolder}#title{font-size:16px;color:#212121;font-weight:600;margin-bottom:10px}hr{height:10px;border:0;box-shadow:0 10px 10px -10px #8c8b8b inset}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # Add CSS file
    book.add_item(nav_css)

    # Set the basic spine
    book.spine = spine

    # Write to the file
    epub.write_epub(file_name, book, {})

    print(Back.GREEN + Fore.BLACK + " File " + Back.YELLOW + f" {file_name} " + Back.GREEN + " Successfully Written ")

# Example usage:
title, date, source, main, sources = fetch_json_text("A farsighted approach to tackle nearsightedness  ScienceDaily")
create_epub(title, date, source, main, sources, "A farsighted approach to tackle nearsightedness  ScienceDaily.epub")
