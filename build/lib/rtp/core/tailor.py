from docx import Document

def generate_tailored_resume(jd_keywords, resume_path, output_path):
    """
    根據 JD 關鍵字修改履歷，並輸出新檔案。
    現階段是 MVP 階段：僅將關鍵詞加到履歷開頭做示意。
    """
    # 載入履歷
    doc = Document(resume_path)

    # 建立新段落：列出所有關鍵詞
    intro = "🔑 JD Keywords:\n" + "\n".join(f"- {kw}" for kw in jd_keywords)
    doc.paragraphs[0].insert_paragraph_before(intro)

    # 儲存新履歷
    doc.save(output_path)
    print(f"✅ Tailored resume saved to: {output_path}")
