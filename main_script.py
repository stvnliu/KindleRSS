import feedparser as fp
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
    for entry in news_feed.entries:
        choice = input(f"Download the post \"{entry.title}\"? (y/N/-y for all RSS entries): ") if not gloabl_yes else "y"
        if choice.lower() == "y":
            extract_text_html(entry)
        elif choice.lower() == "-y":
            gloabl_yes = True
            extract_text_html(entry)
        elif choice.upper() == "N":
            break
        else:
            print("Please enter y/N")


fetch_rss_info("https://www.sciencedaily.com/rss/top.xml")

'''
rss_url = str(input("Enter RSS url: "))
fetch_rss_info(rss_url)
'''
