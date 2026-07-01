import datetime
import os
from PIL import Image

def get_d_m_y():
    now = datetime.datetime.now()
    return f'{now.month}-{now.day}-{now.year}'

if __name__ == "__main__":
    dmy = get_d_m_y()
    year = dmy.split('-')[2]

    title = input("Title > ")
    slug = input("Slug (use hyphens) > ")
    description = input("Description > ")
    tags = input("Tags (comma separated) > ").split(',')

    content = f"""---
title: "{title}"
description: "{description}"
date: {dmy}
slug: {slug}
tags: {tags}
authors: ["flocto"]
image: "./hero.png"
---

CONTENT HERE"""
    
    dir_path = f'src/content/blog/{year}/{slug}'
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, 'index.mdx')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    img = Image.new('RGBA', (1200, 630), color = (0, 0, 0, 0))
    img.save(os.path.join(dir_path, 'hero.png'))

    print(f"Blog post created at {file_path} with placeholder hero.png")