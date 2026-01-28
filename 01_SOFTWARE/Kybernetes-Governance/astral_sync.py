import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_astral_state():
    """Retrieves current calendar events to determine the user's activity state."""
    creds = None
    token_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/01_SOFTWARE/token.json")
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.expanduser("~/Desktop/L'AXE HYBRIDE/01_SOFTWARE/credentials.json"), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return "IDLE"
    
    event_summary = events[0]['summary'].upper()
    if "WORK" in event_summary or "FOCUS" in event_summary:
        return "HIGH_INTENSITY"
    elif "REST" in event_summary or "SLEEP" in event_summary:
        return "REGENERATION"
    return "NEUTRAL"