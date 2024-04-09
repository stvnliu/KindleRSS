from ebooklib import epub


def generate_section(
    index: str,
    heading: str,
    author: str,
    date: str,
    paragraphs: list
) -> tuple:
    # Include the title and published date in the content
    fmt_html = ""
    for text in paragraphs:
        fmt_html += f"<p>{text}</p>"
    content = f"\
        <h1>{heading}</h1>\
        <h3><i>{author}</i></h3>\
        <h4>Published on: {date}</h4>\
        "\
        + fmt_html

    section = epub.EpubHtml(
        file_name=f"{index}.xhtml", title=heading, content=content)
    return (section, epub.Link(f"{index}.xhtml", heading, heading))
