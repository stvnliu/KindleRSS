from ebooklib import epub
def generate_section( index: str, heading: str, summary: str, paragraphs: list(str) ) -> tuple(epub.EpubHtml, epub.Link):
    section = epub.EpubHtml(file_name=f"{index}.xhtml", title=heading, content="\n".join(paragraphs))
    return (section, epub.Link(f"{index}.xhtml", heading, heading))    
