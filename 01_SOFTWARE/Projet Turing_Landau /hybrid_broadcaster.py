import os
import smtplib
import sys
from email.mime.text import MIMEText

# Path for Zoo Analyzer
sys.path.append(os.path.abspath("01_SOFTWARE/Entropic-Zoo-Protocol"))
import zoo_analyzer

def broadcast_hybrid():
    # 1. LOCAL NOTIFICATION (The Reflex)
    title = "AXE HYBRIDE"
    msg = "Resonance Summary Generated."
    os.system(f"osascript -e 'display notification \"{msg}\" with title \"{title}\" sound name \"Crystal\"'")
    print("📢 Local Notification Sent.")

    # 2. EXTERNAL EMAIL (The Archive)
    # Configuration for Gmail or iCloud (Free)
    SMTP_SERVER = "smtp.gmail.com" # or smtp.mail.me.com for iCloud
    SMTP_PORT = 587
    SENDER_EMAIL = "your_other_email@gmail.com"
    SENDER_PWD = "YOUR_APP_PASSWORD" # Create this in Google/Apple Security settings
    RECEIVER = "moc.g3c.protocol@proton.me"

    # Capture the analysis
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        zoo_analyzer.analyze_zoo()
    content = f.getvalue()

    message = MIMEText(f"Resonance Signature:\n\n{content}")
    message["Subject"] = "AXE HYBRIDE - External Echo"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PWD)
            server.sendmail(SENDER_EMAIL, RECEIVER, message.as_string())
        print(f"🌍 External Echo sent to {RECEIVER}")
    except Exception as e:
        print(f"⚠️ External Echo Failed: {e}")

if __name__ == "__main__":
    broadcast_hybrid()