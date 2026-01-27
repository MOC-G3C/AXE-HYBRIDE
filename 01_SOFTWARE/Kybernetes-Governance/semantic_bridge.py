import pyperclip # IMPORTANT: Requires 'pip install pyperclip' [cite: 2026-01-22]
import os

def scan_clipboard_for_wisdom():
    """Captures transhumanist or philosophical keywords from clipboard."""
    text = pyperclip.paste()
    if not text or len(text) > 500: return None
    
    # Keywords filter
    keywords = ["consciousness", "tesla", "simulation", "entropy", "cybernetic", "vibration"]
    
    if any(key in text.lower() for key in keywords):
        vocab_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE/01_SOFTWARE/Entropic-Zoo-Protocol/custom_vocab.txt")
        
        # Avoid duplicates
        existing = []
        if os.path.exists(vocab_path):
            with open(vocab_path, "r") as f: existing = f.read().splitlines()
        
        if text not in existing:
            with open(vocab_path, "a") as f:
                f.write(text + "\n")
            return text
    return None