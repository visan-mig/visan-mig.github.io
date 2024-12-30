import os
import re

def fix_frontmatter(directory):
    # Get all .md files in the directory
    for filename in os.listdir(directory):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace double --- at the start with single ---
        fixed_content = re.sub(r'^---\s*---', '---', content)
        
        # Write the fixed content back
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(fixed_content)
        
        print(f"Fixed {filename}")

# Run the script
if __name__ == "__main__":
    news_items_dir = "_news_items"  # Change this if your directory is different
    if os.path.exists(news_items_dir):
        fix_frontmatter(news_items_dir)
        print("All files processed!")
    else:
        print(f"Directory {news_items_dir} not found!")