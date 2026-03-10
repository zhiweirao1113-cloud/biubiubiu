# 📚 biubiubiu 的论文知识库

## 目录结构

```
papers/
├── originals/          # 原始 PDF 文件
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
├── summaries/          # 论文摘要（Markdown）
│   ├── attention-is-all-you-need.md
│   └── llama3-paper.md
├── notes/              # 阅读笔记
│   └── YYYY-MM-DD-论文名.md
└── scripts/            # 处理脚本
    ├── extract_pdf.py
    └── generate_summary.py
```

---

## 使用方法

### 1. 放入 PDF
```bash
cp ~/Downloads/*.pdf papers/originals/2026/
```

### 2. 批量处理
```bash
cd papers/scripts
python3 process_all.py
```

### 3. 检索论文
```
你："我读过关于 transformer 的论文吗？"
我：（搜索 summaries/ 文件夹）
```

---

## 摘要模板

每篇论文的摘要包含：

- **标题**: 论文标题
- **作者**: 作者列表
- **日期**: 阅读日期
- **链接**: arXiv/DOI 链接
- **关键词**: 3-5 个关键词
- **核心贡献**: 1-2 句话
- **方法**: 主要技术方法
- **结果**: 关键实验结果
- **我的笔记**: 个人思考和启发
- **相关论文**: 关联的其他论文

---

## 检索方式

### 关键词搜索
```bash
grep -r "transformer" summaries/
```

### 语义搜索
```
你："找一下我读过的关于注意力机制的论文"
```

### 按主题分类
- 🤖 大语言模型
- 🎨 图像生成
- 🗣️ 语音处理
- 📊 强化学习
- 🔒 安全对齐

---

最后更新：2026-03-10
