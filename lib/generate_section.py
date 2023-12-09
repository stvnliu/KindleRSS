from ebooklib import epub

def generate_section(index: str, heading: str, paragraphs: list) -> tuple:
    # Include the title in the content
    content = f"<h1>{heading}</h1>\n" + "\n".join(paragraphs)
    
    section = epub.EpubHtml(file_name=f"{index}.xhtml", title=heading, content=content)
    return (section, epub.Link(f"{index}.xhtml", heading, heading))
