# main.py
import os
import fitz  # PyMuPDF
import json
from utils import find_common_font_sizes, classify_heading

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    spans = []
    
    # Collect all spans (text + size + page)
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text and len(text.split()) < 20 and any(char.isprintable() for char in text):  # Skip long paragraphs and added multilingual support
                            spans.append({
                                "text": text,
                                "size": round(span["size"], 1),
                                "font": span["font"],
                                "page": page_num
                            })
    # print(spans)
    
    # Step 1: Identify font sizes (for title and headings)
    font_order = find_common_font_sizes(spans)
    
    # Step 2: Identify title (biggest font, first page)
    # Step 1: Find max font size on page 1
    max_size_on_page1 = max(span["size"] for span in spans if span["page"] == 1)

    # Step 2: Get all spans at that size (in order)
    title_spans = [
        span for span in spans
        if span["page"] == 1 and span["size"] == max_size_on_page1 and len(span["text"].strip()) > 2
    ]

    # Step 3: Group them into a sentence (remove obvious repeats/partials)
    seen = set()
    title_parts = []
    for span in title_spans:
        clean_text = span["text"].strip()
        if clean_text not in seen:
            title_parts.append(clean_text)
            seen.add(clean_text)

    # Step 4: Join into a full title
    title = " ".join(title_parts)

    
    # Step 3: Identify H1, H2, H3
    outline = []
    for span in spans:
        level = classify_heading(span["size"], font_order)
        if level:
            outline.append({
                "level": level,
                "text": span["text"],
                "page": span["page"]
            })
    print(outline)

    return {
        "title": title,
        "outline": outline
    }

if __name__ == "__main__":
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            print(f"Processing: {filename}")
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline(pdf_path)

            # Save result to output/
            json_filename = filename.replace(".pdf", ".json")
            with open(os.path.join(output_dir, json_filename), "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2,ensure_ascii=False)
            print(f"✅Saved to output/{json_filename}")
