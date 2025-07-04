# TronLink 开发者文档迁移实施指南

## 第一步：创建 GitHub 仓库

### 1.1 创建新仓库
```bash
# 在 GitHub 上创建新仓库
# 仓库名：tronlink-docs
# 描述：TronLink 开发者文档
# 公开仓库
# 初始化时添加 README.md
```

### 1.2 克隆仓库到本地
```bash
git clone https://github.com/your-username/tronlink-docs.git
cd tronlink-docs
```

## 第二步：设置 Jekyll 环境

### 2.1 创建 Jekyll 配置文件
创建 `_config.yml` 文件：

```yaml
# Jekyll 配置
title: TronLink 开发者文档
description: TronLink 钱包开发者文档，包含移动端、插件钱包和 DApp 开发指南
baseurl: ""
url: "https://your-username.github.io"

# 构建设置
markdown: kramdown
highlighter: rouge
permalink: pretty

# 插件
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap

# 集合
collections:
  docs:
    output: true
    permalink: /:collection/:name/

# 默认设置
defaults:
  - scope:
      path: ""
      type: "docs"
    values:
      layout: "docs"

# 排除文件
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor
  - .git
```

### 2.2 创建 Gemfile
```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.2.0"
gem "jekyll-feed", "~> 0.12"
gem "jekyll-seo-tag", "~> 2.6"
gem "jekyll-sitemap", "~> 1.4"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.6"
  gem "jekyll-sitemap", "~> 1.4"
end
```

## 第三步：创建基础模板

### 3.1 创建布局文件
创建 `_layouts/default.html`：

```html
<!DOCTYPE html>
<html lang="{{ page.lang | default: 'zh-CN' }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} - {% endif %}{{ site.title }}</title>
    <meta name="description" content="{{ page.description | default: site.description }}">
    <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
    {% seo %}
</head>
<body>
    {% include navigation.html %}
    
    <div class="container">
        <div class="sidebar">
            {% include sidebar.html %}
        </div>
        
        <main class="content">
            {{ content }}
        </main>
    </div>
    
    {% include footer.html %}
    
    <script src="{{ '/assets/js/search.js' | relative_url }}"></script>
</body>
</html>
```

### 3.2 创建导航组件
创建 `_includes/navigation.html`：

```html
<nav class="navbar">
    <div class="nav-container">
        <div class="nav-brand">
            <a href="{{ '/' | relative_url }}">
                <img src="{{ '/assets/images/logo.png' | relative_url }}" alt="TronLink" class="logo">
                <span class="brand-text">开发者文档</span>
            </a>
        </div>
        
        <div class="nav-menu">
            <a href="{{ '/docs/introduction' | relative_url }}">介绍</a>
            <a href="{{ '/docs/mobile' | relative_url }}">移动端</a>
            <a href="{{ '/docs/plugin-wallet' | relative_url }}">插件钱包</a>
            <a href="{{ '/docs/dapp' | relative_url }}">DApp</a>
        </div>
        
        <div class="nav-search">
            <input type="text" id="search-input" placeholder="搜索文档...">
        </div>
    </div>
</nav>
```

## 第四步：创建文档结构

### 4.1 创建文档目录
```bash
mkdir -p _docs/{mobile,plugin-wallet,dapp}
mkdir -p _docs/mobile/{asset-management,deeplink,dapp-support}
mkdir -p _docs/plugin-wallet/{active-requests,passive-messages}
mkdir -p assets/{css,js,images}
mkdir -p _layouts _includes
```

### 4.2 创建首页
创建 `index.md`：

```markdown
---
layout: default
title: TronLink 开发者文档
---

# TronLink 开发者文档

欢迎使用 TronLink 开发者文档！TronLink 是波场 TRON 生态的去中心化钱包，提供完整的开发者工具和 API。

## 快速开始

- [介绍](/docs/introduction) - 了解 TronLink 和波场生态
- [移动端开发](/docs/mobile) - 移动端集成指南
- [插件钱包](/docs/plugin-wallet) - 浏览器插件开发
- [DApp 开发](/docs/dapp) - 去中心化应用开发

## 主要功能

### 移动端
- 资产管理
- DeepLink 集成
- DApp 浏览器支持

### 插件钱包
- 主动请求功能
- 被动消息接收
- 网站连接管理

### DApp 开发
- 多签转账
- 消息签名
- 普通转账
- Stake2.0

## 技术支持

- [GitHub Issues](https://github.com/your-username/tronlink-docs/issues)
- [社区讨论](https://github.com/your-username/tronlink-docs/discussions)
```

## 第五步：内容迁移

### 5.1 从原文档提取内容
使用以下方法提取原文档内容：

1. **手动复制** - 直接从网页复制内容
2. **爬虫工具** - 使用 Python 脚本批量提取
3. **API 获取** - 如果原文档提供 API

### 5.2 创建 Python 爬虫脚本
创建 `scripts/extract_docs.py`：

```python
import requests
from bs4 import BeautifulSoup
import os
import re

def extract_documentation():
    """从 TronLink 文档网站提取内容"""
    
    # 文档页面列表
    pages = [
        {
            'url': 'https://docs-zh.tronlink.org/',
            'title': '介绍',
            'filename': 'introduction.md'
        },
        {
            'url': 'https://docs-zh.tronlink.org/hd-wallet',
            'title': 'HD 钱包',
            'filename': 'hd-wallet.md'
        },
        # 添加更多页面...
    ]
    
    for page in pages:
        try:
            response = requests.get(page['url'])
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 提取主要内容
            content = soup.find('div', class_='content')
            if content:
                # 转换为 Markdown
                markdown_content = convert_to_markdown(content)
                
                # 保存文件
                with open(f'_docs/{page["filename"]}', 'w', encoding='utf-8') as f:
                    f.write(f"---\n")
                    f.write(f"title: {page['title']}\n")
                    f.write(f"---\n\n")
                    f.write(markdown_content)
                    
                print(f"已提取: {page['title']}")
                
        except Exception as e:
            print(f"提取失败 {page['title']}: {e}")

def convert_to_markdown(element):
    """将 HTML 元素转换为 Markdown"""
    # 这里需要实现 HTML 到 Markdown 的转换逻辑
    # 可以使用 html2text 库
    pass

if __name__ == "__main__":
    extract_documentation()
```

## 第六步：设置 GitHub Pages

### 6.1 启用 GitHub Pages
1. 进入仓库设置
2. 找到 "Pages" 选项
3. 选择 "Deploy from a branch"
4. 选择 `main` 分支和 `/ (root)` 目录
5. 点击 "Save"

### 6.2 创建 GitHub Actions 工作流
创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v2
      
    - name: Setup Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: 3.0
        
    - name: Install dependencies
      run: |
        gem install bundler
        bundle install
        
    - name: Build site
      run: bundle exec jekyll build
      
    - name: Deploy to GitHub Pages
      if: github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./_site
```

## 第七步：样式和功能

### 7.1 创建样式文件
创建 `assets/css/main.scss`：

```scss
---
---

// 变量
$primary-color: #007bff;
$secondary-color: #6c757d;
$background-color: #f8f9fa;
$text-color: #212529;

// 基础样式
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: $text-color;
    margin: 0;
    padding: 0;
}

.container {
    display: flex;
    min-height: 100vh;
}

.sidebar {
    width: 280px;
    background: $background-color;
    border-right: 1px solid #dee2e6;
    padding: 1rem;
}

.content {
    flex: 1;
    padding: 2rem;
    max-width: 800px;
}

// 导航栏样式
.navbar {
    background: white;
    border-bottom: 1px solid #dee2e6;
    padding: 1rem 0;
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
}

// 代码高亮
pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 4px;
    padding: 1rem;
    overflow-x: auto;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-size: 0.9em;
}
```

### 7.2 添加搜索功能
创建 `assets/js/search.js`：

```javascript
// 搜索功能实现
class DocSearch {
    constructor() {
        this.searchInput = document.getElementById('search-input');
        this.searchResults = document.getElementById('search-results');
        this.init();
    }
    
    init() {
        this.searchInput.addEventListener('input', (e) => {
            this.performSearch(e.target.value);
        });
    }
    
    async performSearch(query) {
        if (query.length < 2) {
            this.hideResults();
            return;
        }
        
        // 这里可以实现本地搜索或调用搜索 API
        const results = await this.searchContent(query);
        this.displayResults(results);
    }
    
    async searchContent(query) {
        // 实现搜索逻辑
        // 可以使用 lunr.js 或其他搜索库
        return [];
    }
    
    displayResults(results) {
        // 显示搜索结果
    }
    
    hideResults() {
        // 隐藏搜索结果
    }
}

// 初始化搜索
document.addEventListener('DOMContentLoaded', () => {
    new DocSearch();
});
```

## 第八步：测试和部署

### 8.1 本地测试
```bash
# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000 查看效果
```

### 8.2 部署检查
1. 推送代码到 GitHub
2. 检查 GitHub Actions 是否成功
3. 访问 GitHub Pages 链接验证效果
4. 检查所有链接是否正常工作

## 第九步：优化和维护

### 9.1 SEO 优化
- 添加 meta 标签
- 生成 sitemap
- 优化页面标题和描述

### 9.2 性能优化
- 压缩 CSS 和 JS
- 优化图片
- 启用缓存

### 9.3 内容更新
- 建立内容更新流程
- 设置定期检查机制
- 接受社区贡献

## 常见问题解决

### 问题1：Jekyll 构建失败
**解决方案：**
- 检查 `_config.yml` 语法
- 确保所有 Markdown 文件格式正确
- 查看 GitHub Actions 日志

### 问题2：样式不生效
**解决方案：**
- 检查 CSS 文件路径
- 确保 SCSS 文件有正确的 front matter
- 清除浏览器缓存

### 问题3：搜索功能不工作
**解决方案：**
- 检查 JavaScript 文件是否正确加载
- 验证搜索索引是否正确生成
- 测试搜索 API 是否可用

## 后续扩展

1. **多语言支持** - 添加英文版本
2. **版本控制** - 支持文档版本管理
3. **API 文档** - 集成 Swagger 或类似工具
4. **交互式示例** - 添加可运行的代码示例
5. **社区功能** - 添加评论和反馈系统 