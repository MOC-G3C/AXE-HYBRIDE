import os
from fpdf import FPDF # Requires 'pip install fpdf' [cite: 2026-01-26]

class LegacyPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "GRAND LIVRE DE L'AXE HYBRIDE - 2026", 0, 1, 'C')

def compile_grand_livre():
    """Aggregates all project documentation into a single PDF legacy file."""
    root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
    pdf = LegacyPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    sections = ["01_SOFTWARE", "02_HUMAIN", "03_HARDWARE"]
    
    for section in sections:
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"AXIS: {section}", 0, 1, 'L')
        
        section_path = os.path.join(root_path, section)
        if os.path.exists(section_path):
            for file in os.listdir(section_path):
                if file.endswith(".md"):
                    pdf.set_font("Arial", 'B', 12)
                    pdf.cell(0, 10, f"> File: {file}", 0, 1, 'L')
                    pdf.set_font("Arial", '', 10)
                    with open(os.path.join(section_path, file), 'r') as f:
                        content = f.read().encode('latin-1', 'ignore').decode('latin-1')
                        pdf.multi_cell(0, 5, content)
    
    output_path = os.path.join(root_path, "02_HUMAIN/GRAND_LIVRE_AXE_HYBRIDE.pdf")
    pdf.output(output_path)
    return output_path