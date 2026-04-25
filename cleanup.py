import os
import re
import shutil

mapping = {
    "강경태": "kyungtaekang",
    "강다영": "dayoungkang",
    "강동준": "dongjunkang",
    "곽봉석": "bongseokkwak",
    "김솔아": "solakim",
    "김수민": "suminkim",
    "김영수": "yeongsukim",
    "민태홍": "taehongmin",
    "박세현": "sehyunpark",
    "박찬곤": "changonpark",
    "배재훈": "jaehunbae",
    "송세화": "sehwasong",
    "안상아": "sangaan",
    "이경수": "kyungsulee",
    "이동현": "donghyunlee",
    "이준호": "junholee",
    "이진선": "jinsunlee",
    "정세진": "sejinjeong",
    "정진영": "jinyoungjeong",
    "최서연": "seoyeonchoi",
    "최홍석": "hongseokchoi",
    "홍건하": "geonhahong",
    "홍사강": "sakanghong",
    "吳恩達": "alicewu",
    "admin": "kyungsulee"
}

base_path = "content/en/authors"

def update_authors_folder():
    # 1. Handle Professor Lee first
    ksl_path = os.path.join(base_path, "kyungsulee")
    admin_path = os.path.join(base_path, "admin")
    lee_ko_path = os.path.join(base_path, "이경수")
    
    # Ensure kyungsulee exists and has correct content
    if os.path.exists(ksl_path):
        # We'll use the content from kyungsulee as the master English content
        pass
    elif os.path.exists(admin_path):
        # If kyungsulee doesn't exist but admin does, rename admin to kyungsulee
        os.rename(admin_path, ksl_path)
    
    # Delete 이경수 if it exists
    if os.path.exists(lee_ko_path):
        shutil.rmtree(lee_ko_path)
        
    # If admin still exists (and it wasn't renamed), we'll delete it later after updating references
    # Actually, let's just delete it now if kyungsulee exists
    if os.path.exists(admin_path) and os.path.exists(ksl_path) and admin_path != ksl_path:
        shutil.rmtree(admin_path)

    # 2. Handle other folders
    for old_name, new_name in mapping.items():
        if old_name in ["admin", "이경수", "kyungsulee"]:
            continue
            
        old_dir = os.path.join(base_path, old_name)
        new_dir = os.path.join(base_path, new_name)
        
        if os.path.exists(old_dir):
            if old_dir != new_dir:
                if os.path.exists(new_dir):
                    print(f"Merging {old_dir} into {new_dir}")
                    for f in os.listdir(old_dir):
                        src = os.path.join(old_dir, f)
                        dst = os.path.join(new_dir, f)
                        if os.path.isdir(src):
                            if os.path.exists(dst):
                                shutil.rmtree(dst)
                            shutil.move(src, dst)
                        else:
                            shutil.move(src, dst)
                    os.rmdir(old_dir)
                else:
                    os.rename(old_dir, new_dir)
            
            # Update _index.md
            index_path = os.path.join(new_dir, "_index.md")
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update authors:
                # We want to replace the first item or all items in the authors list
                content = re.sub(r'authors:\s*\n(\s*-\s*).+', f'authors:\n\\1{new_name}', content)
                
                # Ensure slug exists and matches
                if 'slug:' in content:
                    content = re.sub(r'slug:\s*.+', f'slug: {new_name}', content)
                else:
                    # Insert slug after authors
                    content = re.sub(r'(authors:\s*\n\s*-\s*.+)', f'\\1\nslug: {new_name}', content)
                
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)

    # Final check for kyungsulee folder's _index.md
    ksl_index = os.path.join(base_path, "kyungsulee", "_index.md")
    if os.path.exists(ksl_index):
        with open(ksl_index, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'authors:\s*\n(\s*-\s*).+', f'authors:\n\\1kyungsulee', content)
        if 'slug:' in content:
            content = re.sub(r'slug:\s*.+', f'slug: professor', content) # Keep professor slug as requested
        else:
            content = re.sub(r'(authors:\s*\n\s*-\s*.+)', f'\\1\nslug: professor', content)
        with open(ksl_index, 'w', encoding='utf-8') as f:
            f.write(content)

def update_all_references():
    for root, dirs, files in os.walk("content/en"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                changed = False
                
                # Update authors in front matter
                for old_name, new_name in mapping.items():
                    # Match "- old_name" within authors block
                    pattern = r'(\s*-\s*)' + re.escape(old_name) + r'(\s*\n)'
                    if re.search(pattern, content):
                        content = re.sub(pattern, f'\\1{new_name}\\2', content)
                        changed = True
                
                # Task 4: Remove Korean text
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    body = parts[2]
                    
                    # Remove Korean from body
                    if re.search(r'[가-힣]', body):
                        # Remove (Korean)
                        body = re.sub(r'\s*\([가-힣\s]+\)', '', body)
                        # Remove remaining Korean words
                        body = re.sub(r'[가-힣]+', '', body)
                        parts[2] = body
                        changed = True
                        
                    # Remove Korean from front matter fields
                    for field in ['abstract', 'publication', 'summary', 'title', 'award_name', 'award_event']:
                        pattern = rf'({field}:\s*[\'"]?)(.*?[가-힣].*?)([\'"]?\s*\n)'
                        if re.search(pattern, front_matter):
                            def remove_korean(match):
                                val = match.group(2)
                                # Remove Korean but keep the rest
                                clean_val = re.sub(r'[가-힣]', '', val).strip()
                                # Clean up extra separators or empty parentheses
                                clean_val = re.sub(r'\(\s*\)', '', clean_val).strip()
                                return f"{match.group(1)}{clean_val}{match.group(3)}"
                            front_matter = re.sub(pattern, remove_korean, front_matter)
                            changed = True
                    parts[1] = front_matter
                    content = '---'.join(parts)

                if changed:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

if __name__ == "__main__":
    update_authors_folder()
    update_all_references()
