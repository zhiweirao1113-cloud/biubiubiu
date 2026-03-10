# biubiubiu - Personal Academic Website

个人学术网站 - Micro-LED 研究者 biubiubiu 的个人主页

## 📁 文件结构

```
website-deploy/
├── index.html          # 主页面（桌面版）
├── mobile.html         # 移动端优化版本
├── papers/             # 论文 PDF 文件夹
│   └── originals/      # 6 篇发表论文 PDF
└── README.md           # 本文件
```

## 🚀 部署方案

### 方案 1: GitHub Pages（推荐）⭐

**优点**: 免费、稳定、自定义域名

**步骤**:

1. **创建 GitHub 仓库**
   ```bash
   # 在 GitHub.com 上
   # 1. 登录 GitHub
   # 2. 点击右上角 + → New repository
   # 3. 仓库名：biubiubiu-website
   # 4. 选择 Public
   # 5. 点击 Create repository
   ```

2. **上传文件**
   ```bash
   # 方法 A: 使用 Git
   git init
   git add .
   git commit -m "Initial commit - biubiubiu website"
   git remote add origin https://github.com/YOUR_USERNAME/biubiubiu-website.git
   git push -u origin main
   
   # 方法 B: GitHub 网页上传
   # 在仓库页面点击 "uploading an existing file"
   # 拖拽所有文件上传
   ```

3. **启用 GitHub Pages**
   ```
   # 在 GitHub 仓库页面
   1. 点击 Settings
   2. 左侧菜单选择 Pages
   3. Source 选择 "main branch"
   4. 点击 Save
   5. 等待 1-2 分钟
   ```

4. **获得链接**
   ```
   你的网站链接：
   https://YOUR_USERNAME.github.io/biubiubiu-website/
   ```

---

### 方案 2: Vercel（最简单）⚡

**优点**: 拖拽上传、自动 HTTPS、快速

**步骤**:

1. **访问 Vercel**
   ```
   https://vercel.com/new
   ```

2. **登录/注册**
   - 可以用 GitHub 账号登录

3. **部署**
   ```
   1. 点击 "Add New Project"
   2. 选择 "Deploy"
   3. 拖拽 website-deploy 文件夹
   4. 等待部署完成（约 30 秒）
   ```

4. **获得链接**
   ```
   你的网站链接：
   https://biubiubiu-website.vercel.app
   ```

---

### 方案 3: Netlify（同样简单）🎈

**步骤**:

1. **访问 Netlify**
   ```
   https://app.netlify.com/drop
   ```

2. **拖拽上传**
   ```
   直接把 website-deploy 文件夹拖到页面
   ```

3. **获得链接**
   ```
   你的网站链接：
   https://random-name-12345.netlify.app
   ```

---

## 📱 移动端版本

- **桌面版**: `index.html`（功能完整）
- **移动版**: `mobile.html`（手机优化）

部署后访问：
- 桌面版：`https://你的域名.com/`
- 移动版：`https://你的域名.com/mobile.html`

---

## 📊 网站特性

- ✅ 响应式设计（手机/平板/电脑适配）
- ✅ 一键翻译（中文/英文）
- ✅ 论文下载（6 篇 PDF）
- ✅ 研究统计展示
- ✅ 时间线展示
- ✅ 现代化 UI 设计

---

## 🔧 自定义

### 修改内容

编辑 `index.html` 文件：
- 搜索中文内容直接修改
- 修改 `data-en` 属性更新英文翻译

### 添加新论文

在 `papers/originals/` 添加 PDF，然后在 HTML 中添加对应的下载链接。

---

## 📈 访问统计（可选）

### 添加 Google Analytics

1. 注册 Google Analytics
2. 获取跟踪代码
3. 粘贴到 `index.html` 的 `<head>` 标签内

### 使用 Vercel/Netlify 自带统计

- Vercel: Dashboard → Analytics
- Netlify: Dashboard → Analytics

---

## 🎯 推荐方案

**首次部署**: 用 **Vercel**（最简单，30 秒上线）

**长期使用**: 用 **GitHub Pages**（更稳定，可自定义域名）

---

## 📞 网站链接示例

部署成功后，你的网站链接会是：

```
GitHub Pages:
https://biubiubiu.github.io/website/

Vercel:
https://biubiubiu-website.vercel.app

Netlify:
https://biubiubiu.netlify.app
```

可以直接分享给任何人！📱💻

---

## ⚠️ 注意事项

1. **PDF 文件较大**: 确保上传了所有 PDF 文件
2. **相对路径**: 下载链接使用相对路径，确保 papers 文件夹结构正确
3. **隐私**: 确认所有公开的信息都是你愿意分享的

---

*Created: 2026-03-10*
*By: Evan AI Assistant*
