import os
import re

def generate_gallery_view():
    """Parses the Oracle logs to create a permanent art gallery HTML."""
    oracle_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02Humain/ORACLE_MESSAGES.md")
    gallery_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE_GALLERY.html")
    
    if not os.path.exists(oracle_path):
        return "No visions found to display."

    with open(oracle_path, "r") as f:
        content = f.read()

    # Extracting messages and images using regex [cite: 2026-01-26]
    entries = re.findall(r'### \[(.*?)\] - (.*?)\n> "(.*?)"\n\n!\[Vision\]\((.*?)\)', content)
    
    html_items = ""
    for resonance, time, msg, img in reversed(entries):
        html_items += f"""
        <div class="art-card">
            <img src="{img}" alt="Vision">
            <div class="info">
                <p class="timestamp">{time} | {resonance}</p>
                <p class="quote">"{msg}"</p>
            </div>
        </div>
        """

    gallery_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MUSEUM MODE - AXE HYBRIDE</title>
        <style>
            body {{ background: #000; color: #fff; font-family: 'Helvetica', sans-serif; padding: 50px; text-align: center; }}
            .gallery {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; }}
            .art-card {{ width: 350px; border: 1px solid #333; transition: 0.5s; filter: grayscale(100%); }}
            .art-card:hover {{ filter: grayscale(0%); border-color: #00ffff; transform: scale(1.05); }}
            img {{ width: 100%; height: 350px; object-fit: cover; }}
            .info {{ padding: 15px; background: #0a0a0a; text-align: left; }}
            .timestamp {{ font-size: 10px; color: #00ffff; margin: 0; }}
            .quote {{ font-style: italic; font-size: 14px; margin-top: 10px; }}
            h1 {{ letter-spacing: 10px; font-weight: 100; margin-bottom: 50px; color: #00ffff; }}
        </style>
    </head>
    <body>
        <h1>AXE HYBRIDE GALLERY</h1>
        <div class="gallery">{html_items}</div>
    </body>
    </html>
    """
    
    with open(gallery_path, "w") as f:
        f.write(gallery_html)
    return True