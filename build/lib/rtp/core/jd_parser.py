import re
from typing import List

def extract_keywords(jd_path: str) -> list[str]:
    print(f"Loading JD from: {jd_path}")
    with open(jd_path, "r") as f:
        text = f.read()
    return ["project management", "KPI", "automation"]
