import os
from pathlib import Path
import re
from urllib.parse import unquote

def clean_url(url):
    """Clean up a URL by removing quotes and fixing encoded spaces"""
    url = url.strip('"\'')
    url = url.replace('%20', ' ')
    url = re.sub(r'(?<!:)//+', '/', url)
    return url

def fix_urls(directory="_posts"):
    """
    Fixes URL encoding and YAML front matter issues in markdown files:
    1. Properly quotes Liquid syntax in YAML front matter
    2. Fixes encoded {{ site.baseurl }} syntax
    3. Removes duplicate pdf paths
    4. Ensures proper link formatting
    """
    posts_dir = Path(directory)
    
    if not posts_dir.exists():
        print(f"Directory {directory} not found!")
        return
    
    markdown_files = list(posts_dir.glob("*.md"))
    
    for file_path in markdown_files:
        print(f"Processing {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split content into front matter and body
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]
            
            # Fix pdf_link in front matter
            front_matter = re.sub(
                r'(pdf_link:\s*)(.*?)(\n|$)',
                lambda m: f'pdf_link: "{{ site.baseurl }}{clean_url(unquote(unquote(m.group(2).replace("{{ site.baseurl }}", ""))))}"\n',
                front_matter
            )
            
            # Reconstruct content with fixed front matter
            content = f"---{front_matter}---{body}"
        
        # Fix inline markdown links
        content = re.sub(
            r'(\[.*?\]\()(\{\{\s*site\.baseurl\s*\}\})?(/pdfs/.*?)(\))',
            lambda m: f'{m.group(1)}{{{{ site.baseurl }}}}{clean_url(unquote(unquote(m.group(3))))}{m.group(4)}',
            content
        )
        
        # Remove duplicate /pdfs/ in paths
        content = content.replace('/pdfs/pdfs/', '/pdfs/')
        
        # Write the fixed content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Fixed {file_path.name}")

if __name__ == "__main__":
    fix_urls()
    print("Done!")