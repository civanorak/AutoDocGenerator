import os
import re

def escape_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to escape < and > but NOT in code blocks
    # Code blocks are marked by ``` or `
    
    # Simple strategy: find code blocks and parts between them
    # This is a bit complex for a regex, so let's do it part by part
    
    parts = re.split(r'(```.*?```|`.*?`)', content, flags=re.DOTALL)
    
    new_parts = []
    for i, part in enumerate(parts):
        # Even parts are outside code blocks, odd parts are inside
        if i % 2 == 0:
            # Escape < and > but avoid escaping existing &lt; or already correct HTML if any
            part = part.replace('<', '&lt;').replace('>', '&gt;')
        new_parts.append(part)
        
    new_content = ''.join(new_parts)
    
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def process_directory(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        # Skip .vitepress and node_modules
        if '.vitepress' in root or 'node_modules' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                if escape_md_file(path):
                    count += 1
                    print(f"Fixed: {path}")
    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
    process_directory(docs_dir)
