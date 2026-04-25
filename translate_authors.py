import os
import yaml
import shutil

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

def translate_role(role):
    for ko, en in role_map.items():
        if ko in role:
            return role.replace(ko, en)
    return role

def translate_org(org):
    return org_map.get(org, org)

def translate_interests(interests):
    if not interests:
        return interests
    interest_map = {
        '인공지능 (AI)': 'AI',
        'Vision & Language': 'Vision & Language',
        '의료수학 (Medical Mathematics)': 'Medical Mathematics',
        '항공우주 (Aerospace)': 'Aerospace',
        '콘텐츠 (Contents)': 'Contents',
        '개발 (Development & Deploy)': 'Development & Deploy'
    }
    return [interest_map.get(i, i) for i in interests]

for author_name in os.listdir(ko_authors_dir):
    ko_author_path = os.path.join(ko_authors_dir, author_name)
    if not os.path.isdir(ko_author_path):
        continue
    
    en_author_path = os.path.join(en_authors_dir, author_name)
    if not os.path.exists(en_author_path):
        os.makedirs(en_author_path)
    
    # Copy avatar if exists
    for f in os.listdir(ko_author_path):
        if f.startswith('avatar'):
            shutil.copy(os.path.join(ko_author_path, f), os.path.join(en_author_path, f))
    
    ko_index_path = os.path.join(ko_author_path, '_index.md')
    if not os.path.exists(ko_index_path):
        continue
        
    with open(ko_index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split('---')
    if len(parts) < 3:
        continue
        
    front_matter = yaml.safe_load(parts[1])
    body = parts[2]
    
    if author_name in ['admin', '이경수']:
        # Already handled or will be handled specially
        continue
        
    # Translate title
    if 'name_en' in front_matter:
        front_matter['title'] = front_matter['name_en']
    
    # Translate role
    if 'role' in front_matter:
        front_matter['role'] = translate_role(front_matter['role'])
        
    # Translate organizations
    if 'organizations' in front_matter:
        for org in front_matter['organizations']:
            if 'name' in org:
                org['name'] = translate_org(org['name'])
    
    # Translate bio
    if 'bio' in front_matter and front_matter['bio']:
        # bio is usually long, but let's try a simple replacement if it's just a repetition of research interests
        pass # Will need manual touch if it's complex, but for students it's often empty or placeholder
        
    # Translate interests
    if 'interests' in front_matter:
        front_matter['interests'] = translate_interests(front_matter['interests'])
        
    # Translate education
    if 'education' in front_matter and 'courses' in front_matter['education']:
        for course in front_matter['education']['courses']:
            if 'course' in course:
                course['course'] = translate_role(course['course'])
            if 'institution' in course:
                course['institution'] = translate_org(course['institution'])

    # Write translated file
    new_content = '---\n' + yaml.dump(front_matter, allow_unicode=True) + '---\n' + body
    with open(os.path.join(en_author_path, '_index.md'), 'w', encoding='utf-8') as f:
        f.write(new_content)

