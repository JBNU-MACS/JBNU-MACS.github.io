import os
import shutil
import re

ko_authors_dir = 'content/ko/authors/'
en_authors_dir = 'content/en/authors/'

role_map = {
    '조교수': 'Assistant Professor',
    '석사과정': "Master's Student",
    '박사과정': 'PhD Student',
    '학부연구생': 'Undergraduate Researcher',
    '파트석사': "Part-time Master's Student",
    '졸업생': 'Alumni',
    '연구원': 'Researcher',
    '박사후연구원': 'Postdoctoral Researcher',
}

org_map = {
    '전북대학교 컴퓨터인공지능학부': 'School of Computer and Artificial Intelligence, Jeonbuk National University',
    '전북대학교 전자.정보공학부(컴퓨터공학)': 'Department of Electronic and Information Engineering (Computer Science), Jeonbuk National University',
    '한국환경공단': 'Korea Environment Corporation',
    '포항공과대학교 (POSTECH)': 'Pohang University of Science and Technology (POSTECH)',
    '대구경북과학기술원 (DGIST)': 'Daegu Gyeongbuk Institute of Science and Technology (DGIST)',
    'Harvard Medical School': 'Harvard Medical School',
    '전북대학교': 'Jeonbuk National University',
    '한동대학교': 'Handong Global University',
}

interest_map = {
    '인공지능 (AI)': 'AI',
    'Vision & Language': 'Vision & Language',
    '의료수학 (Medical Mathematics)': 'Medical Mathematics',
    '항공우주 (Aerospace)': 'Aerospace',
    '콘텐츠 (Contents)': 'Contents',
    '개발 (Development & Deploy)': 'Development & Deploy'
}

def translate_role(text):
    for ko, en in role_map.items():
        text = text.replace(ko, en)
    return text

def translate_org(text):
    for ko, en in org_map.items():
        text = text.replace(ko, en)
    return text

def translate_interests(text):
    for ko, en in interest_map.items():
        text = text.replace(ko, en)
    return text

for author_name in os.listdir(ko_authors_dir):
    if author_name in ['admin', '이경수']:
        continue
    
    ko_author_path = os.path.join(ko_authors_dir, author_name)
    if not os.path.isdir(ko_author_path):
        continue
    
    en_author_path = os.path.join(en_authors_dir, author_name)
    if not os.path.exists(en_author_path):
        os.makedirs(en_author_path)
    
    # Copy files
    for f in os.listdir(ko_author_path):
        if f.startswith('avatar'):
            shutil.copy(os.path.join(ko_author_path, f), os.path.join(en_author_path, f))
    
    ko_index_path = os.path.join(ko_author_path, '_index.md')
    if not os.path.exists(ko_index_path):
        continue
        
    with open(ko_index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic translation via regex
    content = translate_role(content)
    content = translate_org(content)
    content = translate_interests(content)
    
    # Try to find name_en and set title to it
    name_en_match = re.search(r'name_en:\s*"([^"]+)"', content)
    if name_en_match:
        name_en = name_en_match.group(1)
        content = re.sub(r'title:\s*.+', f'title: {name_en}', content, count=1)
    
    with open(os.path.join(en_author_path, '_index.md'), 'w', encoding='utf-8') as f:
        f.write(content)

