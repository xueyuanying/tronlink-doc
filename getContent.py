#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import requests
from bs4 import BeautifulSoup
# from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse
import time
import json

BASE_URL = "https://docs.tronlink.org/"
LANGS = {
    'en': '',  # 英文版本是根路径
    'zh': 'zh/'  # 中文版本路径
}
SAVE_ROOT = "docs"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

def get_page_content(url):
    """获取页面内容"""
    try:
        print(f"正在获取: {url}")
        resp = requests.get(url, headers=HEADERS, timeout=15)
        
        if resp.status_code != 200:
            print(f"[WARN] HTTP {resp.status_code} for {url}")
            return None
        
        return resp.text
    except Exception as e:
        print(f"[ERROR] Failed to get {url}: {e}")
        return None

def extract_navigation_from_html(html_content):
    """从HTML中提取导航结构"""
    soup = BeautifulSoup(html_content, 'html.parser')
    pages = set()
    
    # 查找所有链接
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if href.startswith('/'):
            # 这是相对路径，需要转换为完整URL
            full_url = urljoin(BASE_URL, href)
            pages.add(full_url)
    
    return list(pages)

def get_known_pages():
    """获取已知的页面路径"""
    return [
        '',  # 首页
        'introduction',
        'hd-wallets',
        'tronlink-app/asset-management',
        'tronlink-app/asset-management/custom-token',
        'tronlink-app/deeplink',
        'tronlink-app/deeplink/open-wallet',
        'tronlink-app/deeplink/open-dapp',
        'tronlink-app/deeplink/login-by-tronlink',
        'tronlink-app/deeplink/transfer',
        'tronlink-app/deeplink/sign-transaction',
        'tronlink-app/deeplink/sign-message',
        'tronlink-app/deeplink/result-code',
        'tronlink-app/dapp-support',
        'tronlink-app/dapp-support/tronlink-integration',
        'tronlink-app/dapp-support/dapp-explorer',
        'tronlink-wallet-extension/request-tronlink-extension',
        'tronlink-wallet-extension/request-tronlink-extension/connect-website',
        'tronlink-wallet-extension/request-tronlink-extension/add-token',
        'tronlink-wallet-extension/receive-messages-from-tronlink',
        'tronlink-wallet-extension/receive-messages-from-tronlink/account-change-message',
        'tronlink-wallet-extension/receive-messages-from-tronlink/network-change-message',
        'tronlink-wallet-extension/receive-messages-from-tronlink/successful-connection-message',
        'tronlink-wallet-extension/receive-messages-from-tronlink/disconnect-website-message',
        'tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated',
        'tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-rejects-connection',
        'tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-disconnects-from-the-website',
        'tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-accepts-connection',
        'tronlink-wallet-extension/receive-messages-from-tronlink/messages-to-be-deprecated/user-requests-to-connect-to-the-website',
        'dapp/start-developing',
        'dapp/multi-signature-transfer',
        'dapp/message-signature',
        'dapp/general-transfer',
        'dapp/stake2.0'
    ]

def get_all_page_urls(lang):
    """获取所有页面URL"""
    pages = set()
    
    # 首先获取主页内容
    main_url = urljoin(BASE_URL, LANGS[lang])
    html_content = get_page_content(main_url)
    
    if html_content:
        # 从主页提取导航
        nav_pages = extract_navigation_from_html(html_content)
        pages.update(nav_pages)
    
    # 添加已知路径
    known_paths = get_known_pages()
    for path in known_paths:
        url = urljoin(BASE_URL, LANGS[lang] + path)
        pages.add(url)
    
    return list(pages)

def extract_content_from_html(html_content):
    """从HTML中提取主要内容"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 尝试找到主要内容区域
    main_content = None
    
    # 查找main标签
    main = soup.find('main')
    if main:
        main_content = main
    
    # 如果没有找到main，尝试其他选择器
    if not main_content:
        # 查找包含内容的div
        content_divs = soup.find_all('div', class_=re.compile(r'content|main|article'))
        if content_divs:
            main_content = content_divs[0]
    
    # 如果还是没有找到，使用body
    if not main_content:
        main_content = soup.find('body')
    
    if not main_content:
        return None
    
    return str(main_content)

def save_content_to_markdown(content, url, lang):
    """保存内容为markdown文件"""
    if not content:
        return False
    
    # 转换为markdown
    md_content = md(content, heading_style="ATX")
    
    # 生成本地文件路径
    path = urlparse(url).path
    # 移除语言前缀
    if lang == 'zh':
        path = path.replace('/zh/', '/')
    elif lang == 'en':
        path = path.replace('/en/', '/')
    
    # 处理根路径
    if path == '/' or path == '':
        rel_path = 'index'
    else:
        rel_path = path.strip('/')
    
    # 确保是markdown文件
    if not rel_path.endswith('.md'):
        rel_path += '.md'
    
    md_path = os.path.join(SAVE_ROOT, lang, rel_path)
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"[OK] {md_path}")
    return True

def process_language(lang):
    """处理单个语言版本"""
    print(f"==== 开始处理 {lang} 版本 ====")
    
    # 获取所有页面URL
    urls = get_all_page_urls(lang)
    print(f"找到 {len(urls)} 个页面")
    
    successful_count = 0
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] 处理: {url}")
        
        # 获取页面内容
        html_content = get_page_content(url)
        if not html_content:
            continue
        
        # 提取内容
        content = extract_content_from_html(html_content)
        if not content:
            print(f"[WARN] No content found for {url}")
            continue
        
        # 保存为markdown
        if save_content_to_markdown(content, url, lang):
            successful_count += 1
        
        time.sleep(0.5)  # 避免请求过快
    
    print(f"==== {lang} 版本处理完成: {successful_count}/{len(urls)} 成功 ====")
    return successful_count

def main():
    total_successful = 0
    total_count = 0
    
    for lang in LANGS:
        successful = process_language(lang)
        total_successful += successful
        total_count += len(get_all_page_urls(lang))
    
    print(f"==== 全部处理完成: {total_successful}/{total_count} 成功 ====")

if __name__ == '__main__':
    main() 