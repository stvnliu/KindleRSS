import feedparser as fp
import os
from lib.convert import bulk_epub
from lib.generate_metadata import metadata_gen
from lib.rss import extract_text_html
from datetime import date
from lib.send_to_kindle import send_file


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
        choice = input(f"Download the post \"{
                       entry.title}\"? (y/N/-y for all RSS entries): ") if not gloabl_yes else "y"
        if choice.lower() == "y":
            titles.append(extract_text_html(entry))
        elif choice.lower() == "-y":
            gloabl_yes = True
            titles.append(extract_text_html(entry))
        elif choice.upper() == "N":
            break
        else:
            print("Please enter y/N")

    print(f"Generating metadata file for collection with feed title: {
          news_feed.feed.title}")
    success = metadata_gen(news_feed.feed.title, titles)

    if success:
        print("Metadata generation succeeded!")
    else:
        print("Metadata generation failed!")

    print("Starting EPUB generation process...")

    if not os.path.exists("./out"):
        os.mkdir("./out")

    # get the date when the program is ran
    today_date = str(date.today())

    # add date in the end of the book title
    success = bulk_epub(f"./out/{news_feed.feed.title} {today_date}.epub")
    print("EPUB Generation successful! Book located at ./out/ directory.") if success else print("EPUB generation failed!")

    print("*" * 10)
    # Haven't tested this function yet
    flag_send = str(input("Send to Kindle[y/N]"))

    if flag_send.lower() == "y":
        print("Start send to Kindle function...")
        send_file(f"./out/{news_feed.feed.title} {today_date}.epub")

    elif flag_send.lower() == "n":
        pass

    else:
        print("Please enter valid choice [y/N]")


# This is just an example RSS url
fetch_rss_info("https://www.sciencedaily.com/rss/top.xml")

'''
rss_url = str(input("Enter RSS url: "))
fetch_rss_info(rss_url)
'''
