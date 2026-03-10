# 📚 论文知识库使用指南

## 快速开始

### 1️⃣ 准备 PDF 文件

```bash
# 把你的论文 PDF 放到这个文件夹
~/.openclaw/workspace/papers/originals/

# 可以按年份分类
papers/originals/2024/
papers/originals/2025/
papers/originals/2026/
```

### 2️⃣ 安装依赖

```bash
# 选项 1: 使用 pypdf（轻量）
pip3 install pypdf

# 选项 2: 使用 pdfplumber（更准确）
pip3 install pdfplumber
```

### 3️⃣ 批量处理

```bash
cd ~/.openclaw/workspace/papers/scripts

# 处理 originals 文件夹中的所有 PDF
python3 process_pdf.py --input ../originals --output ../summaries

# 或者处理单个文件
python3 process_pdf.py --single ~/Downloads/attention-paper.pdf --output ../summaries
```

### 4️⃣ 查看结果

```bash
# 查看生成的摘要
ls ../summaries/

# 查看索引
cat ../summaries/INDEX.md

# 阅读某篇论文摘要
cat ../summaries/attention-is-all-you-need.md
```

---

## 🔍 如何让我检索论文

### 方式 1: 直接问我

```
你："我读过关于 transformer 的论文吗？"

我：（搜索 summaries/ 文件夹）
"找到了！你读过 3 篇相关论文：
1. Attention Is All You Need (2017)
2. Transformer-XL
3. ..."
```

### 方式 2: 关键词搜索

```
你："搜索关键词：attention, transformer"

我：（grep + 语义搜索）
"找到 5 篇相关论文，最相关的是..."
```

### 方式 3: 按主题询问

```
你："我读过哪些大语言模型相关的论文？"

我：（根据关键词分类）
"你读过 12 篇 LLM 相关论文，包括：
- LLaMA 系列
- GPT 系列
- ..."
```

---

## 📝 如何补充笔记

每篇论文的摘要是自动生成的，你可以补充个人笔记：

```bash
# 编辑摘要文件
nano ../summaries/论文名.md

# 填写这些部分：
## 💡 核心贡献
## 🔬 方法
## 📊 实验结果
## 🤔 我的思考
```

或者告诉我：

```
你："给 attention-is-all-you-need.md 添加笔记：
这篇论文的核心是自注意力机制，抛弃了 RNN..."

我：（更新文件）
"✅ 已添加笔记！"
```

---

## 🎯 高级用法

### 1. 创建论文阅读清单

```bash
# 创建待读列表
cat > ../to-read.md << EOF
# 📖 待读论文

- [ ] Paper 1.pdf
- [ ] Paper 2.pdf
- [x] Paper 3.pdf (已读)
EOF
```

### 2. 建立论文关联

在摘要文件中添加：

```markdown
## 📚 相关论文

- [[attention-is-all-you-need]] 基础论文
- [[transformer-xl]] 改进版本
- [[bert]] 应用
```

### 3. 定期复习

```bash
# 创建复习提醒
cat > ../review-schedule.md << EOF
# 📅 论文复习计划

## 本周复习
- attention-is-all-you-need.md
- bert.md

## 本月复习
- 所有 LLM 相关论文
EOF
```

---

## 🤖 我可以帮你做什么

### ✅ 我能做的

| 任务 | 说明 |
|------|------|
| 🔍 搜索论文 | 按关键词、主题、作者搜索 |
| 📊 统计分析 | "我读了多少篇论文？" |
| 💡 总结归纳 | "总结所有 attention 相关论文" |
| 🔗 关联推荐 | "和这篇论文相关的还有哪些？" |
| 📝 提取引用 | "帮我提取 BibTeX 引用" |
| 📈 趋势分析 | "我的阅读趋势如何？" |

### ❌ 我做不到的

| 任务 | 原因 |
|------|------|
| 理解数学公式 | PDF 提取后公式会丢失 |
| 分析图表 | 只能处理文本 |
| 运行代码 | 需要额外配置 |

---

## 📊 示例工作流

```
1. 下载论文
   ↓
2. 放入 originals/
   ↓
3. 运行 process_pdf.py
   ↓
4. 阅读生成的摘要
   ↓
5. 补充个人笔记
   ↓
6. 告诉我："我读了这篇论文，核心是..."
   ↓
7. 我记住并建立关联
   ↓
8. 下次询问时，我能回忆起来
```

---

## 🔧 故障排除

### 问题 1: PDF 无法提取文本

```bash
# 可能是扫描版 PDF
# 解决：使用 OCR 工具
pip3 install pytesseract
```

### 问题 2: 提取的文本乱码

```bash
# 可能是编码问题
# 解决：手动创建摘要文件
```

### 问题 3: 找不到某篇论文

```bash
# 检查文件名
ls ../summaries/ | grep 关键词

# 或者全文搜索
grep -r "关键词" ../summaries/
```

---

## 📞 需要帮助？

```
你："帮我处理 papers/originals/ 里的所有 PDF"
你："搜索我读过的关于 RLHF 的论文"
你："总结我所有论文笔记"
```

---

最后更新：2026-03-10
由 Evan AI Assistant 创建 🤖
