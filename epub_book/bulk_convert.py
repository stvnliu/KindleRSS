import json
from epub_book.generate_section import generate_section
from ebooklib import epub

def bulk_epub(filename: str, metadata_file_loc: str = "../rss/metadata.json"):
    with open(metadata_file_loc, "r") as file:
        metadata = json.loads(file.read())
        file.close()
    book = epub.EpubBook()
    book.set_identifier("1145141919810")
    book.set_title(articledata["feed_title"])
    book.set_language('en')

    # Initialize Table of Contents (TOC) and spine
    toc = []
    spine = ['nav']
    index = 1
    for article in metadata["collection"]:
        with open(f"{article}.json", "r") as articleFile:
            articledata = json.loads(articleFile.read())
            articleFile.close()
        
        # Create main content item (EpubHtml)
        main_item, epub_link = generate_section(
            str(index),
            article["title"][0],
            article["summary"][0],
            article["story"]
        )
        book.add_item(main_item)
        # Add main content to TOC and spine
        toc.append(epub_link)
        spine.append(main_item)
        index += 1
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
    epub.write_epub(filename, book, {})
    return