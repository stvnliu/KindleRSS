import json
def metadata_gen(feed_title: str,
                 article_files: list, 
                 filename: str = "./rss/metadata.json"):
    data = {
        "feed_title": feed_title,
        "collection": article_files
    }
    with open(filename, "w+") as file:
        file.write(json.dumps(data, indent=4))
        file.close()
    return True
def metadata_read():
    return