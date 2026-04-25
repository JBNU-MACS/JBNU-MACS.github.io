import os
import shutil
import re

ko_posts_dir = 'content/ko/post/'
en_posts_dir = 'content/en/post/'

post_translations = {
    '24-03-02-신임교원임용': {
        'title': '(Spring 2024) Joined School of Computer and Artificial Intelligence, Jeonbuk National University',
        'body': 'Professor Kyungsu Lee appointed to the School of Computer and Artificial Intelligence, Jeonbuk National University.\n\n<!--more-->\n'
    },
    '24-11-20-K-Health-수상': {
        'title': '(Fall 2024) Awarded at K-Health Medical AI Hackathon',
        'body': 'Congratulations!\n\nUndergraduate researchers Dayoung Kang, Sumin Kim, Sehyun Park, and Seo-Yeon Choi from MacsLAB won the Grand Prize at the 2024 K-Health Medical AI Hackathon.\n\nThe competition focused on developing an AI model for breast mass segmentation using mammography image data. The students developed, trained, and tuned their own segmentation model, achieving high validation performance by utilizing public datasets in addition to the provided dataset, leading to their victory.'
    },
    '25-10-15-AIxMHC2025-Best-Poster-Award': {
        'title': '(AIxMHC 2025) Best Poster Award',
        'body': 'Congratulations!\n\nThe team of **Seo-Yeon Choi, Haeyun Lee, and Kyungsu Lee** from MacsLAB won the **Best Poster Award** at **AIxMHC 2025**.\n\nThe award-winning paper is:\n\n- **Statistical Multi-Modal Fusion for Patient-Centric Medical Diagnosis Using DICOM**\n\n![Best Poster Award Certificate](aixmhc2025-award-certificate.jpeg)\n*AIxMHC 2025 Best Poster Award Certificate*\n\n![AIxMHC 2025 Scene](aixmhc2025-team.jpeg)\n*AIxMHC 2025 Team Photo*\n\n![Poster Presentation](aixmhc2025-poster.jpeg)\n*Poster Presentation Scene*\n\nMacsLAB will continue to strive for clinically meaningful research achievements in the field of medical AI.\n\nRelated Links:\n- [/publication/0036-statistical-multi-modal-fusion-for-patient-centric-medical-diagnosis-using-dicom/](/publication/0036-statistical-multi-modal-fusion-for-patient-centric-medical-diagnosis-using-dicom/)\n- [AIxMHC 2025](https://chaoneng.github.io/aixmhc2025.github.io/)'
    },
    '25-11-08-KOSOMBE-우수포스터상': {
        'title': '(2025 KOSOMBE) Sagang Hong Won Best Poster Award',
        'body': 'Congratulations!\n\n**Sagang Hong**, a Master\'s student at MacsLAB, won the **Best Poster Award** at the **2025 Fall Conference of the Korean Society of Medical and Biological Engineering (KOSOMBE)**.\n\nThis achievement recognizes his outstanding research presented at the conference held from November 6 to 8, 2025, at Inje University (Gimhae).\n\n![Sagang Hong Winning the Best Poster Award](kosombe2025-award-hong.jpeg)\n*KOSOMBE 2025 Fall Conference Award Ceremony*\n\n![Best Poster Award Certificate](kosombe2025-award-certificate.jpeg)\n*Best Poster Award Certificate for Sagang Hong*\n\nAward-winning Paper Information:\n\n- **Sagang Hong (1st author), Junyoung Kim, Kyungsu Lee (Corresponding author)**\n- **SAM2-based Bayesian Prompt Adaptation for Cross-Modality Medical Segmentation**\n\nWe sincerely congratulate Sagang Hong on his award and look forward to more excellent research achievements from MacsLAB.\n\nRelated Links:\n- [/publication/0034-sam2-based-bayesian-prompt-adaptation-for-cross-modality-medical-segmentation/](/publication/0034-sam2-based-bayesian-prompt-adaptation-for-cross-modality-medical-segmentation/)\n- [KOSOMBE 2025 Fall Conference Program](https://www.kosombe.or.kr/register/2025_fall/program/sub07.html)'
    }
}

for post_name in os.listdir(ko_posts_dir):
    ko_post_path = os.path.join(ko_posts_dir, post_name)
    if not os.path.isdir(ko_post_path):
        continue
    
    en_post_path = os.path.join(en_posts_dir, post_name)
    if not os.path.exists(en_post_path):
        os.makedirs(en_post_path)
    
    # Copy all files from ko to en
    for f in os.listdir(ko_post_path):
        if f != 'index.md':
            shutil.copy(os.path.join(ko_post_path, f), os.path.join(en_post_path, f))
    
    ko_index_path = os.path.join(ko_post_path, 'index.md')
    if not os.path.exists(ko_index_path):
        continue
        
    with open(ko_index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if post_name in post_translations:
        trans = post_translations[post_name]
        # Replace title
        content = re.sub(r'title:\s*.+', f'title: {trans["title"]}', content, count=1)
        # Replace body (everything after the second ---)
        parts = content.split('---')
        if len(parts) >= 3:
            new_content = '---' + parts[1] + '---\n\n' + trans['body']
            content = new_content
    else:
        # For those already in English or mostly English, just copy but maybe fix some Korean bits
        content = content.replace('학부연구생', 'Undergraduate Researcher')
        content = content.replace('석사과정', "Master's Student")
        content = content.replace('박사과정', 'PhD Student')
    
    with open(os.path.join(en_post_path, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(content)

