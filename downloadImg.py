import requests
from bs4 import BeautifulSoup
import os
import time
import html2text
from urllib.parse import urljoin, urlparse

BASE_URL = "https://docs.tronlink.org/"
SAVE_DIR = "downloaded_docs"
IMG_DIR = os.path.join(SAVE_DIR, "images")
HEADERS = {"User-Agent": "Mozilla/5.0"}

# 初始化 html2text 转换器
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.body_width = 0

os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

def scrape_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def download_image(img_url, page_name, index):
    parsed = urlparse(img_url)
    ext = os.path.splitext(parsed.path)[1] or ".jpg"
    filename = f"{page_name}_img_{index}{ext}"
    local_path = os.path.join("images", filename)
    full_path = os.path.join(SAVE_DIR, local_path)

    try:
        img_data = requests.get(img_url, headers=HEADERS).content
        with open(full_path, "wb") as f:
            f.write(img_data)
        return local_path  # 返回用于替换 Markdown 的相对路径
    except Exception as e:
        print(f"❌ 图片下载失败 {img_url} ：{e}")
        return img_url  # 保留原路径作为兜底

# 抓取首页
index_page = scrape_page(BASE_URL)
if not index_page:
    exit()

soup = BeautifulSoup(index_page, "html.parser")
links = set()

# 收集所有页面链接
for link in soup.select('a.toclink'):
    href = link.get("href")
    if href and not href.startswith(("http", "#")):
        links.add(href)

# 抓取所有页面内容 + 图片
for path in links:
    url = urljoin(BASE_URL, path)
    print(f"📄 下载页面：{url}")

    html = scrape_page(url)
    if not html:
        continue

    page_soup = BeautifulSoup(html, "html.parser")
    content = page_soup.select_one(".page-default-width")

    if not content:
        continue

    page_name = path.strip("/").replace("/", "_") or "index"

    # 下载页面中所有图片并替换 src
    img_tags = content.find_all("img")
    for idx, img in enumerate(img_tags):
        src = img.get("src")
        if not src:
            continue
        full_img_url = urljoin(url, src)
        local_path = download_image(full_img_url, page_name, idx)
        img["src"] = local_path  # 替换为本地路径

    # 转 Markdown
    markdown_content = h.handle(str(content))

    # 保存为 .md 文件
    filename = os.path.join(SAVE_DIR, f"{page_name}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    time.sleep(1)

print("✅ 所有页面与图片已导出完成！")