import feedparser as fp
from metadata_gen import metadata_gen
from rss_functions import extract_text_html

def fetch_rss_info(url):
    news_feed = fp.parse(url)
    for entry in news_feed.entries:
        print("Post Tile: ", entry.title)
        print("Post Tile Detail: ", entry.title_detail)
        print("Date published: ", entry.published)
        # print("Summary: ", entry.summary)
        print("****************************************")
    gloabl_yes = False
    print('Number of RSS posts: ', len(news_feed.entries))
    print('Feed Title: ', news_feed.feed.title)
    print("Entry keys: ", news_feed.keys())
    titles = []
    for entry in news_feed.entries:
        choice = input(f"Download the post \"{entry.title}\"? (y/N/-y for all RSS entries): ") if not gloabl_yes else "y"
        if choice.lower() == "y":
            titles.append(extract_text_html(entry))
        elif choice.lower() == "-y":
            gloabl_yes = True
            titles.append(extract_text_html(entry))
        elif choice.upper() == "N":
            break
        else:
            print("Please enter y/N")
    print(f"Generating metadata file for collection with feed title: {news_feed.feed.title}")
    success = metadata_gen(news_feed.feed.title, titles)
    if success:
        print("Metadata generation succeeded!")
    else:
        print("Metadata generation failed!")


fetch_rss_info("https://www.sciencedaily.com/rss/top.xml")

'''
rss_url = str(input("Enter RSS url: "))
fetch_rss_info(rss_url)
'''
