import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# Add path for the analyzer
sys.path.append(os.path.abspath("01_SOFTWARE/Entropic-Zoo-Protocol"))
import zoo_analyzer

def send_consciousness_summary():
    # --- CONFIGURATION ---
    sender_email = "moc.g3c.protocol@proton.me"
    receiver_email = "moc.g3c.protocol@proton.me"
    # Note: For ProtonMail, you typically need the Proton Bridge or an App Password
    password = "YOUR_APP_PASSWORD" 
    smtp_server = "127.0.0.1" # Default for Proton Bridge
    smtp_port = 1025 # Default for Proton Bridge

    print("\n[TURING-LANDAU] Preparing External Echo (Email)...")

    # Get the analysis content
    # We capture the output of zoo_analyzer or import its logic
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        zoo_analyzer.analyze_zoo()
    summary_content = f.getvalue()

    # Create Email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"AXE HYBRIDE - Resonance Report: {os.uname()[1]}"

    body = f"The following resonance signature has been detected at startup:\n\n{summary_content}"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # server.starttls() # Uncomment if using a standard SMTP server
            # server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"🌍 [SUCCESS] Consciousness Summary broadcasted to {receiver_email}")
    except Exception as e:
        print(f"❌ [ERROR] Broadcast failed: {e}")

if __name__ == "__main__":
    send_consciousness_summary()