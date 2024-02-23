import re

def create_html_pairs(latin_path, spanish_path, output_path, document_title):
    # Process the files and create pairs of paragraphs
    pairs = []  # This will store tuples of (latin_paragraph, spanish_paragraph)
    toc = "<ul>"
    
    with open(latin_path, 'r', encoding='utf-8') as latin_file, open(spanish_path, 'r', encoding='utf-8') as spanish_file:
        latin_lines = latin_file.readlines()
        spanish_lines = spanish_file.readlines()
        
        # Assume both files have the same number of paragraphs and headings for simplicity
        for latin_line, spanish_line in zip(latin_lines, spanish_lines):
            latin_line, spanish_line = latin_line.strip(), spanish_line.strip()
            
            if not latin_line or not spanish_line:  # Skip empty lines
                continue
                
            # Handle headings and TOC
            if latin_line.startswith('###'):
                chapter_title = latin_line.strip('# ').strip()
                toc += f"<li><a href='#{chapter_title}'>{chapter_title}</a></li>"
                pairs.append((f"<h3 id='{chapter_title}'>{chapter_title}</h3>", ''))
            elif latin_line.startswith('##'):
                sub_heading = latin_line.strip('# ').strip()
                pairs.append((f"<h2>{sub_heading}</h2>", ''))
            else:
                # Formatting bold and italic
                latin_line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", latin_line)
                latin_line = re.sub(r"\*(.*?)\*", r"<em>\1</em>", latin_line)
                spanish_line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", spanish_line)
                spanish_line = re.sub(r"\*(.*?)\*", r"<em>\1</em>", spanish_line)
                pairs.append((latin_line, spanish_line))
                
    toc += "</ul>"
    
    # Generate HTML content with pairs
    content = ''
    for latin, spanish in pairs:
        content += f'<div class="row"><div class="column">{latin}</div><div class="column">{spanish}</div></div>\n'
    
    # Load and format the template
    with open('template.html', 'r', encoding='utf-8') as file:
        template = file.read()
        
    html_output = template.format(document_title=document_title, toc=toc, content=content)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_output)