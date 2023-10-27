from google_api_utils import get_contacts, get_calendar_events, get_emails, get_authenticated_service, get_credentials

from data_manipulation import diff_invitees_contacts, compare_emails_to_contacts
import pandas as pd
import csv
import json

#main.py
#TODO Debug CSV files

# All scopes together
ALL_SCOPES = [
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
]

def process_to_dataframe(raw_data):
    # Convert raw data to DataFrame (this will vary depending on your data's structure)
    df = pd.DataFrame(raw_data)
    return df

def save_to_csv(data, filename):
    data.to_csv(filename, index=False)

def main():
    print("Starting data collection...")

    # Initialize common credentials
    creds = get_credentials(ALL_SCOPES)  # Make sure to add this function to google_api_utils.py

    # Fetch and process contacts
    print("Fetching contacts...")
    contacts_data = get_contacts(creds)  # Modify get_contacts to accept creds
    contacts_df = process_to_dataframe(contacts_data)
    print("Contacts fetched. Saving to CSV...")
    save_to_csv(contacts_df, 'output/contacts.csv')

    # Fetch and process calendar events for the last year
    print("Fetching calendar events...")
    calendar_data = get_calendar_events(creds)  # Modify get_calendar_events to accept creds
    calendar_df = process_to_dataframe(calendar_data)
    print("Calendar events fetched. Saving to CSV...")
    save_to_csv(calendar_df, 'output/calendar_events.csv')

    # ... rest of your code ...

    # Fetch and process emails for the last month
    print("Fetching emails...")
    email_data = get_emails(creds)  # Modify get_emails to accept creds
    email_df = process_to_dataframe(email_data)
    print("Emails fetched. Saving to CSV...")
    save_to_csv(email_df, 'output/emails.csv')

    # ... rest of your code ...

if __name__ == "__main__":
    main()
