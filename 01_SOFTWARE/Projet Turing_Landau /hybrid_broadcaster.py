import os
import smtplib
import sys
from email.mime.text import MIMEText

# Accessing the Zoo Analyzer for the 19kb log data
sys.path.append(os.path.abspath("01_SOFTWARE/Entropic-Zoo-Protocol"))
import zoo_analyzer

def broadcast_hybrid():
    """
    Triggers a local macOS notification and relays a resonance 
    report to Proton via Gmail SMTP.
    """
    # 1. LOCAL REFLEX
    os.system("osascript -e 'display notification \"Resonance Summary Dispatched\" with title \"AXE HYBRIDE\"'")
    
    # 2. EXTERNAL RELAY (Gmail to Proton)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    # IMPORTANT: Replace the placeholder below with your actual Gmail address
    SENDER_EMAIL = "MARCO.CORBIN@gmail.com" 
    SENDER_PWD = "hefnemxmwjvmrawm" # Your generated App Password
    RECEIVER = "moc.g3c.protocol@proton.me"

    # Capturing the Zoo Analysis output
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
        print(f"🌍 [SUCCESS] Echo transmitted to {RECEIVER} via Relay.")
    except Exception as e:
        print(f"⚠️ [RELAY ERROR] Check credentials or connection: {e}")

if __name__ == "__main__":
    broadcast_hybrid()