# Adobe-Hackathon

> **🔍 Connecting the Dots Through Docs — Intelligent PDF Outline Extractor**

---

````markdown
# 📄 Intelligent PDF Outline Extractor
### Adobe India Hackathon 2025 – Round 1A: Connecting the Dots Through Docs

## 🚀 Project Summary

This solution automatically extracts structured outlines from unstructured PDF documents. It identifies the **Title** and hierarchical **Headings** (H1, H2, H3) from a given PDF and outputs the results in a clean, standardized `JSON` format.

This enables smarter document experiences such as:
- Document summarization
- Search engine indexing
- Recommendation systems
- Personalized content navigation

---

## 🧠 Problem Statement: Round 1A

> "Given a PDF file, extract a clean and structured document outline that includes the title and headings (H1, H2, H3) along with their corresponding page numbers."

---

## ✅ Features

- 🧠 Detects **Title** + multi-level headings **(H1, H2, H3)**  
- 📄 Handles **up to 50-page PDFs** with ease  
- 🌐 **Multilingual support** (Hindi, Japanese, etc.) via UTF-8  
- 🧱 Completely **Dockerized** for consistent builds  
- 🧠 Uses **font size analysis** and basic heuristics — no ML required  
- 🧊 Fully **offline-compatible** (no network required)

---

## 📁 Input / Output Format

### ✅ Input
Place your `.pdf` files in the `/input` directory (max 50 pages each)

### ✅ Output
Corresponding `.json` files will be saved in `/output` directory in the format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
````

---

## 📦 Project Structure

```
round1a_heading_extractor/
├── input/                 ← Input PDFs go here
├── output/                ← Output JSONs will be saved here
├── main.py                ← Main program
├── utils.py               ← Heading classification helpers
├── requirements.txt       ← Python dependencies
├── Dockerfile             ← Container setup
└── README.md              ← Project documentation
```

## ⚙️ How It Works

1. **Parse PDFs** using PyMuPDF (`fitz`) to extract text spans
2. **Analyze font sizes** on all pages to infer heading hierarchy
3. **Select title** from the largest visible text on Page 1
4. **Classify headings** into H1, H2, H3 using relative font size ranking
5. **Generate structured JSON output** per file
6. **Save results in output/** as UTF-8 encoded `.json` files

## 🏗️ Tech Stack

* 🐍 Python 3.10
* 📚 [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
* 🐳 Docker (platform: `linux/amd64`)

---

## 🧪 Running Locally (Dockerized)

### ✅ 1. Build the Docker Image

```bash
docker build --platform linux/amd64 -t heading-extractor .
```

### ✅ 2. Run the Container

```bash
docker run --rm \-v %cd%/input:/app/input \-v %cd%/output:/app/output \--network none \heading-extractor
```

💡 *(Use `${PWD}` instead of `%cd%` on Mac/Linux/PowerShell)*

Ex: This works on Powershell

```bash
docker run --rm -v "${PWD}/input:/app/input" -v "${PWD}/output:/app/output" --network none round1a_heading_extractor 
```


## 🌍 Multilingual Support

* ✅ Unicode characters preserved in output (`ensure_ascii=False`)
* ✅ Tested on PDFs with:

  * Hindi (`हिंदी पाठ्यक्रम`)
  * Japanese (`人工知能`)
  * English
* ✅ UTF-8 encoded output files

```json
{
  "title": "हिंदी पाठ्यक्रम",
  "outline": [
    { "level": "H1", "text": "निर्देश", "page": 1 },
    ...
  ]
}
```

📝 **Limitation**: Some older PDFs with non-Unicode fonts (e.g., Kruti Dev) may not render text correctly. This is a known PyMuPDF limitation.


## 🔒 Constraint Compliance (Adobe Hackathon)

| Constraint                      | Compliance                            |
| ------------------------------- | ------------------------------------- |
| Execution Time ≤ 10s (50 pages) | ✅ Pass                                |
| Model Size ≤ 200MB (if used)    | ✅ No ML used                          |
| Network Access                  | ✅ Offline enforced (`--network none`) |
| Runtime (CPU-only, amd64 arch)  | ✅ Docker platform set                 |
| Memory                          | ✅ Tested on <500MB RAM                |

---

## 📋 Submission Checklist (Adobe)

✅ Working Dockerfile in root directory
✅ All dependencies installed within container
✅ README with:

* Approach
* Instructions to build/run
* Multilingual and Constraint notes

## 🤖 Approach Summary

* PDF parsing using PyMuPDF
* Heading hierarchy derived by **font size clustering**
* Title detection by largest font on first page
* Clean modular design (`main.py` + `utils.py`)
* UTF-8 compliant, no internet dependency

---

## 📚 Sample Test Case

```bash
input/
└── input1.pdf

output/
└── output1.json
```

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "What is AI?", "page": 1 },
    { "level": "H2", "text": "Narrow AI", "page": 2 },
    { "level": "H3", "text": "Examples", "page": 2 }
  ]
}
```
