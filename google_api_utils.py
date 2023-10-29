from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os

# All scopes together
ALL_SCOPES = [
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
]

CREDENTIALS_FILE = 'env/token.json'

def get_credentials(scopes):
    creds = None

    # Load credentials from the file if it exists
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, scopes)

    # Refresh or obtain new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Use `Request()` as the required argument for `refresh()`
        else:
            flow = InstalledAppFlow.from_client_secrets_file('env/oauth2_credentials.json', scopes)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(CREDENTIALS_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds

# Build the service using credentials
def get_authenticated_service(api, version, creds):
    return build(api, version, credentials=creds)

# Fetch contacts
def get_contacts(creds):
    service = get_authenticated_service('people', 'v1', creds)
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses'
    ).execute()
    print("Data type of get_contacts results: ", type(results))
    # print("First 500 characters of results: ", json.dumps(results, indent=4)[:500])
    return results  # Add this line

# Fetch calendar events
def get_calendar_events(creds):
    service = get_authenticated_service('calendar', 'v3', creds)
    results = service.events().list(calendarId='primary').execute()
    print("Data type of get_calendar_events results: ", type(results))
    # print("First 500 characters of results: ", json.dumps(results, indent=4)[:500])
    return results  # Add this line

# Fetch emails
def get_emails(creds):
    service = get_authenticated_service('gmail', 'v1', creds)
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])
    full_messages = []  # List to hold the full message details
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        full_messages.append(msg)
    return full_messages

if __name__ == "__main__":
    creds = get_credentials(ALL_SCOPES)
    get_contacts(creds)
    get_calendar_events(creds)
    get_emails(creds)
