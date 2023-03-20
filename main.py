import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def main():

    new_str = "✨"+  datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d') + "✨"
    # 获取README.md内容
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    print(new_str)

    new_readme_md_content = re.sub(r'✨(.|\n)*✨', new_str, readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

main()
