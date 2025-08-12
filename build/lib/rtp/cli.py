import typer
from rtp.core.jd_parser import extract_keywords

app = typer.Typer()
parse_app = typer.Typer()

app.add_typer(parse_app, name="parse")


@app.command("parse-jd")
def parse_jd(jd_path: str):
    """
    Parse JD file and extract key terms.
    """
    print(f"Loading JD from: {jd_path}")
    keywords = extract_keywords(jd_path)
    for kw in keywords:
        print(f"- {kw}")


from rtp.core.tailor import generate_tailored_resume

@app.command("tailor")
def tailor(jd_path: str, resume_path: str, output_path: str = "store/tailored.docx"):
    """
    根據 JD 與原始履歷，生成客製化履歷。
    """
    print(f"📄 JD: {jd_path}")
    print(f"📄 Resume: {resume_path}")
    print(f"📤 Output: {output_path}")

    keywords = extract_keywords(jd_path)
    generate_tailored_resume(keywords, resume_path, output_path)


if __name__ == "__main__":
    app()
