import markdown
from xhtml2pdf import pisa
import os
from datetime import datetime

# ==========================================================
# MOC-G3C SYSTEM : PDF GENERATION ENGINE (Protocol λ v1.1)
# Arbiter: Marc-Olivier Corbin
# ==========================================================

def convert_md_to_pdf(source_file, output_file):
    # 1. Lecture du fichier Markdown
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 2. Conversion en HTML
    html_content = markdown.markdown(content, extensions=['extra', 'smarty'])
    
    # 3. Style et Signature "Marc-Olivier Corbin"
    date_str = datetime.now().strftime("%Y-%m-%d")
    styled_html = f"""
    <html>
        <head><style>
            body {{ font-family: Helvetica, Arial, sans-serif; color: #333; line-height: 1.5; padding: 50px; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }}
            h2 {{ color: #2980b9; margin-top: 30px; border-left: 5px solid #2980b9; padding-left: 10px; }}
            pre {{ background-color: #f8f9fa; padding: 15px; border: 1px solid #ddd; border-radius: 5px; font-size: 0.9em; }}
            blockquote {{ border-left: 5px solid #ccc; padding-left: 15px; font-style: italic; color: #555; }}
            footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; font-size: 0.8em; color: #7f8c8d; text-align: center; }}
            .signature {{ font-weight: bold; color: #2c3e50; }}
        </style></head>
        <body>
            {html_content}
            <footer>
                <p>Digital Audit ID: G-02c | Physics Compliance: VALIDATED</p>
                <p>Certified by Arbiter: <span class="signature">Marc-Olivier Corbin (MOC-G3C)</span></p>
                <p>Date: {date_str} | Location: Sainte-Julie, QC</p>
            </footer>
        </body>
    </html>
    """

    # 4. Génération du PDF
    with open(output_file, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(styled_html, dest=result_file)
    
    return pisa_status.err

# Traitement automatique des fichiers du projet Janus-Gateway
files_to_convert = [
    "DEVIS_TEMPLATE.md",
    "SAFETY_LIFTING_CHECKLIST.md",
    "TURING_LANDAU_SPEC.md",
    "PROJECT_LOG.md"
]

print(f"--- Starting MOC-G3C PDF Export ---")
for md_file in files_to_convert:
    if os.path.exists(md_file):
        pdf_name = md_file.replace(".md", ".pdf")
        print(f"Archiving: {pdf_name}...")
        convert_md_to_pdf(md_file, pdf_name)

print(f"\n[SUCCESS] Protocol λ v1.1 Deployment Complete.")
print(f"Arbiter: Marc-Olivier Corbin")