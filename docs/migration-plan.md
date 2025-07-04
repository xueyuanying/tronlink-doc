# TronLink 开发者文档迁移计划

## 项目概述

将 [TronLink 开发者文档](https://docs-zh.tronlink.org/) 从 GitBook 迁移到 GitHub，提供更好的维护性和协作体验。

## 迁移目标

1. **保持内容完整性** - 确保所有现有文档内容完整迁移
2. **改善用户体验** - 提供更好的搜索、导航和阅读体验
3. **支持协作开发** - 通过 GitHub 支持社区贡献
4. **多语言支持** - 保持中英文双语支持
5. **自动化部署** - 通过 GitHub Actions 实现自动部署

## 技术方案

### 推荐方案：GitHub Pages + Jekyll

**优势：**
- 原生支持 Markdown
- 自动生成导航
- 支持搜索功能
- 免费托管
- 易于维护

**技术栈：**
- Jekyll 静态站点生成器
- GitHub Pages 托管
- Markdown 文档格式
- Liquid 模板语言

## 文档结构设计

```
tronlink-docs/
├── _config.yml                    # Jekyll 配置
├── _layouts/                      # 布局模板
│   ├── default.html
│   └── docs.html
├── _includes/                     # 包含文件
│   ├── navigation.html
│   ├── sidebar.html
│   └── footer.html
├── assets/                        # 静态资源
│   ├── css/
│   │   ├── main.scss
│   │   └── syntax-highlighting.scss
│   ├── js/
│   │   └── search.js
│   └── images/
│       ├── logo.png
│       └── screenshots/
├── _docs/                         # 文档内容
│   ├── introduction.md            # 介绍
│   ├── hd-wallet.md              # HD 钱包
│   ├── mobile/                    # 移动端文档
│   │   ├── index.md
│   │   ├── asset-management.md    # 资产管理
│   │   │   └── custom-tokens.md   # 自定义通证
│   │   ├── deeplink.md           # DeepLink
│   │   │   ├── open-wallet.md
│   │   │   ├── open-dapp.md
│   │   │   ├── login-auth.md
│   │   │   ├── transfer.md
│   │   │   ├── transaction-signing.md
│   │   │   ├── message-signing.md
│   │   │   └── callback-codes.md
│   │   └── dapp-support.md       # DApp支持
│   │       ├── integrate-tronlink.md
│   │       └── dapp-browser.md
│   ├── plugin-wallet/            # 插件钱包
│   │   ├── index.md
│   │   ├── active-requests.md    # 主动请求
│   │   │   ├── connect-website.md
│   │   │   └── add-token.md
│   │   └── passive-messages.md   # 被动接收消息
│   │       ├── account-change.md
│   │       ├── network-change.md
│   │       ├── connect-success.md
│   │       └── disconnect.md
│   └── dapp/                     # DApp 开发
│       ├── index.md
│       ├── getting-started.md    # 开始开发
│       ├── multi-sign-transfer.md # 多签转账
│       ├── message-signing.md    # 消息签名
│       ├── transfer.md           # 普通转账
│       └── stake2.md             # Stake2.0
├── index.md                      # 首页
├── README.md                     # 项目说明
└── .github/                      # GitHub 配置
    └── workflows/
        └── deploy.yml            # 自动部署配置
```

## 迁移步骤

### 第一阶段：环境准备
1. 创建 GitHub 仓库 `tronlink-docs`
2. 设置 GitHub Pages
3. 配置 Jekyll 环境
4. 创建基础模板

### 第二阶段：内容迁移
1. 从原文档提取所有内容
2. 转换为 Markdown 格式
3. 整理文档结构
4. 添加导航和链接

### 第三阶段：功能完善
1. 实现搜索功能
2. 添加多语言支持
3. 优化移动端体验
4. 添加代码高亮

### 第四阶段：测试部署
1. 本地测试
2. 部署到 GitHub Pages
3. 功能验证
4. 性能优化

## 时间计划

- **第1周**：环境准备和基础搭建
- **第2-3周**：内容迁移和格式转换
- **第4周**：功能完善和测试
- **第5周**：部署上线和优化

## 维护计划

1. **定期更新** - 每月检查文档更新
2. **社区贡献** - 接受 Pull Request
3. **版本控制** - 使用 Git 管理文档版本
4. **自动化** - 通过 GitHub Actions 自动部署

## 成功标准

1. ✅ 所有原文档内容完整迁移
2. ✅ 搜索功能正常工作
3. ✅ 导航结构清晰
4. ✅ 移动端适配良好
5. ✅ 加载速度优化
6. ✅ 社区可以贡献内容

## 风险评估

1. **内容丢失风险** - 通过详细备份和验证避免
2. **格式转换问题** - 使用自动化工具和人工检查
3. **功能缺失** - 逐步完善功能，确保核心功能优先
4. **用户适应** - 提供迁移说明和引导

## 后续优化

1. **国际化** - 支持更多语言
2. **交互式示例** - 添加可运行的代码示例
3. **API 文档** - 集成 API 文档生成
4. **社区功能** - 添加评论和反馈功能 