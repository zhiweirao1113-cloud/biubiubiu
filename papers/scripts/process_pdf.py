#!/usr/bin/env python3
"""
PDF 论文处理工具
功能：
1. 提取 PDF 文本内容
2. 生成结构化摘要
3. 创建检索索引
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime


def extract_text_from_pdf(pdf_path: str) -> str:
    """从 PDF 提取文本（使用 pypdf 或 pdfplumber）。"""
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except ImportError:
        try:
            import pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text
        except ImportError:
            print("⚠️  需要安装：pip install pypdf 或 pip install pdfplumber")
            return None
    except Exception as e:
        print(f"❌ 提取失败：{e}")
        return None


def extract_metadata(text: str, filename: str) -> dict:
    """从论文文本中提取元数据。"""
    metadata = {
        "filename": filename,
        "title": "",
        "authors": [],
        "abstract": "",
        "keywords": [],
        "sections": [],
        "processed_at": datetime.now().isoformat()
    }
    
    # 尝试提取标题（通常在开头）
    lines = text.split('\n')[:50]
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 20 and len(line) < 200:
            # 可能是标题
            if not metadata["title"]:
                metadata["title"] = line
                break
    
    # 尝试提取摘要
    abstract_patterns = [
        r"Abstract\s*\n(.*?)(?=\n\s*\n|\d\.|\bIntroduction\b)",
        r"摘要\s*\n(.*?)(?=\n\s*\n|\d\.|\b引言\b)",
    ]
    
    for pattern in abstract_patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            metadata["abstract"] = match.group(1).strip()[:2000]
            break
    
    # 如果没有找到摘要，取前 500 字
    if not metadata["abstract"]:
        metadata["abstract"] = text[:500].strip()
    
    # 提取章节
    section_patterns = [
        r"\n(\d+\.\s+[A-Z][^\n]+)",
        r"\n([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s*\n)",
    ]
    
    for pattern in section_patterns:
        sections = re.findall(pattern, text)
        if sections:
            metadata["sections"] = [s.strip() for s in sections[:20]]
            break
    
    # 生成关键词（从标题和摘要中提取）
    title_words = metadata["title"].lower().split()
    abstract_words = metadata["abstract"].lower().split()
    
    # 过滤常见词
    stop_words = {"the", "a", "an", "and", "or", "of", "in", "on", "for", "with", "we", "our", "this", "that"}
    keywords = []
    word_freq = {}
    
    for word in title_words + abstract_words[:200]:
        word = re.sub(r'[^a-z]', '', word)
        if len(word) > 3 and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # 取频率最高的 5 个词
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    metadata["keywords"] = [w[0] for w in sorted_words[:5]]
    
    return metadata


def generate_summary_markdown(metadata: dict, output_path: str):
    """生成 Markdown 格式的论文摘要。"""
    
    md_content = f"""# {metadata['title']}

## 📋 基本信息

- **文件名**: {metadata['filename']}
- **处理时间**: {metadata['processed_at']}
- **关键词**: {', '.join(metadata['keywords']) if metadata['keywords'] else '待添加'}

## 📝 摘要

{metadata['abstract']}

## 📑 章节结构

"""
    
    for section in metadata['sections'][:10]:
        md_content += f"- {section}\n"
    
    md_content += f"""
## 💡 核心贡献

（待填写）

## 🔬 方法

（待填写）

## 📊 实验结果

（待填写）

## 🤔 我的思考

（阅读后填写）

## 🔗 相关链接

- arXiv: （待添加）
- GitHub: （待添加）
- 项目主页：（待添加）

## 📚 相关论文

- （待添加）

---
*由 PDF 处理工具自动生成 | 最后更新：{datetime.now().strftime('%Y-%m-%d')}*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"✅ 已生成摘要：{output_path}")


def process_single_pdf(pdf_path: str, output_dir: str):
    """处理单个 PDF 文件。"""
    pdf_path = Path(pdf_path)
    filename = pdf_path.stem
    
    print(f"📄 处理：{pdf_path.name}")
    
    # 提取文本
    text = extract_text_from_pdf(str(pdf_path))
    if not text:
        print(f"⚠️  跳过：{filename} (无法提取文本)")
        return None
    
    # 提取元数据
    metadata = extract_metadata(text, pdf_path.name)
    
    # 生成摘要
    output_path = Path(output_dir) / f"{filename}.md"
    generate_summary_markdown(metadata, str(output_path))
    
    # 保存完整文本
    text_output = Path(output_dir).parent / "full_text" / f"{filename}.txt"
    text_output.parent.mkdir(exist_ok=True)
    with open(text_output, 'w', encoding='utf-8') as f:
        f.write(text[:100000])  # 限制大小
    
    return metadata


def process_all_pdfs(input_dir: str, output_dir: str):
    """批量处理所有 PDF。"""
    input_path = Path(input_dir)
    pdf_files = list(input_path.glob("*.pdf")) + list(input_path.glob("*.PDF"))
    
    print(f"📚 找到 {len(pdf_files)} 个 PDF 文件")
    print("=" * 50)
    
    results = []
    for i, pdf in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] ", end="")
        result = process_single_pdf(str(pdf), output_dir)
        if result:
            results.append(result)
    
    print("\n" + "=" * 50)
    print(f"✅ 完成！处理了 {len(results)}/{len(pdf_files)} 个 PDF")
    
    # 生成索引
    create_index(results, output_dir)
    
    return results


def create_index(papers: list, output_dir: str):
    """创建论文索引文件。"""
    index_path = Path(output_dir) / "INDEX.md"
    
    # 按关键词分组
    keyword_groups = {}
    for paper in papers:
        for kw in paper.get('keywords', []):
            if kw not in keyword_groups:
                keyword_groups[kw] = []
            keyword_groups[kw].append(paper)
    
    # 生成索引
    md_content = f"""# 📚 论文索引

**总数**: {len(papers)} 篇  
**更新时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 🔍 按关键词分类

"""
    
    for kw, papers_list in sorted(keyword_groups.items()):
        md_content += f"\n### {kw} ({len(papers_list)}篇)\n\n"
        for paper in papers_list:
            title = paper.get('title', 'Unknown')[:80]
            filename = paper.get('filename', '')
            md_content += f"- [{title}]({filename.replace('.pdf', '.md')})\n"
    
    md_content += f"""
---

## 📋 完整列表

| # | 标题 | 关键词 | 处理时间 |
|---|------|--------|----------|
"""
    
    for i, paper in enumerate(papers, 1):
        title = paper.get('title', 'Unknown')[:60]
        keywords = ', '.join(paper.get('keywords', [])[:3])
        time = paper.get('processed_at', '')[:10]
        md_content += f"| {i} | {title} | {keywords} | {time} |\n"
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"📑 已生成索引：{index_path}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="PDF 论文处理工具")
    parser.add_argument("--input", "-i", default="originals", help="PDF 输入目录")
    parser.add_argument("--output", "-o", default="summaries", help="摘要输出目录")
    parser.add_argument("--single", "-s", help="处理单个 PDF 文件")
    
    args = parser.parse_args()
    
    if args.single:
        process_single_pdf(args.single, args.output)
    else:
        process_all_pdfs(args.input, args.output)
