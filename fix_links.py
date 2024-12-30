import os
import re
from urllib.parse import quote

def fix_pdf_path(path):
    # Remove any leading/trailing whitespace
    path = path.strip()
    
    # Add leading slash if missing
    if not path.startswith('/'):
        path = '/' + path
        
    # URL encode the path, preserving forward slashes
    parts = path.split('/')
    encoded_parts = [quote(part) for part in parts]
    return '/'.join(encoded_parts)

def fix_pdf_links(directory):
    for filename in os.listdir(directory):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Fix pdf_link in front matter
        fixed_content = re.sub(
            r'(pdf_link: *)([^\n]+)',
            lambda m: f'{m.group(1)}{fix_pdf_path(m.group(2))}',
            content
        )
        
        # Fix markdown links
        fixed_content = re.sub(
            r'\[([^\]]+)\]\(([^)]+\.pdf)\)',
            lambda m: f'[{m.group(1)}]({fix_pdf_path(m.group(2))})',
            fixed_content
        )
        
        if fixed_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(fixed_content)
            print(f"Fixed links in {filename}")
        else:
            print(f"No changes needed in {filename}")

# Run the script
if __name__ == "__main__":
    news_items_dir = "_news_items"
    if os.path.exists(news_items_dir):
        fix_pdf_links(news_items_dir)
        print("All files processed!")
    else:
        print(f"Directory {news_items_dir} not found!")