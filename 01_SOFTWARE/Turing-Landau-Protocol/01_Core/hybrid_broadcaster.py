import os
import smtplib
import sys
from email.mime.text import MIMEText

# Accès à l'analyseur du Zoo pour les données du log
sys.path.append(os.path.abspath("01_SOFTWARE/Entropic-Zoo-Protocol"))
try:
    import zoo_analyzer
except ImportError:
    zoo_analyzer = None

def broadcast_hybrid():
    # 1. RÉFLEXE LOCAL (Notification macOS)
    os.system("osascript -e 'display notification \"Resonance Summary Dispatched\" with title \"AXE HYBRIDE\"'")
    
    # 2. RELAIS EXTERNE (Gmail -> Proton)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    # Tes informations sécurisées
    SENDER_EMAIL = "marco.corbin@gmail.com" 
    SENDER_PWD = "hefnemxmwjvmrawm" 
    RECEIVER = "moc.g3c.protocol@proton.me"

    # Capture de l'analyse du Zoo
    content = "Anamnesis Analysis Error"
    if zoo_analyzer:
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            zoo_analyzer.analyze_zoo()
        content = f.getvalue()

    message = MIMEText(f"--- BIOMETRIC RESONANCE REPORT ---\n\n{content}")
    message["Subject"] = "AXE HYBRIDE - External Echo"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PWD)
            server.sendmail(SENDER_EMAIL, RECEIVER, message.as_string())
        print(f"🌍 [SUCCESS] Echo transmitted to {RECEIVER} via Gmail Relay.")
    except Exception as e:
        print(f"⚠️ [RELAY ERROR]: {e}")

if __name__ == "__main__":
    broadcast_hybrid()
