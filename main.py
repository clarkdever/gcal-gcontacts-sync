from google_api_utils import get_contacts, get_calendar_events, get_emails, get_credentials
from data_manipulation import diff_invitees_contacts, compare_emails_to_contacts
import logging
import pandas as pd
import json

logging.basicConfig(level=logging.DEBUG)

# All scopes together
ALL_SCOPES = [
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
]

def process_to_dataframe(raw_data, data_type):
    try:
        if data_type == 'contacts':
            df = pd.DataFrame(raw_data['connections'])
        elif data_type == 'calendar':
            df = pd.DataFrame(raw_data['items'])
        elif data_type == 'emails':
            # Adjusted to handle list of dictionaries
            df = pd.DataFrame(raw_data)
        logging.debug(f"Processed DataFrame head: {df.head()}")
        return df
    except Exception as e:
        logging.error(f"An error occurred while processing to DataFrame: {e}")
        return None


def save_to_csv(data, filename):
    try:
        if data is not None:
            logging.debug(f"DataFrame head before saving to CSV: {data.head()}")  
            data.to_csv(filename, index=False)
        else:
            print('Error: DataFrame is None')
    except Exception as e:
        logging.error(f"An error occurred while saving to CSV: {e}")  

def main():
    print("Starting data collection...")

    # Initialize common credentials
    creds = get_credentials(ALL_SCOPES)
    
    # Fetch and process contacts
    try:  
        print("Fetching contacts...")
        contacts_data = get_contacts(creds)
        # logging.debug(f"Raw contacts data: {contacts_data}")  
        contacts_df = process_to_dataframe(contacts_data, 'contacts') 
        print("Contacts fetched. Saving to CSV...")
        save_to_csv(contacts_df, 'output/contacts.csv')
    except Exception as e:
        logging.error(f"An error occurred while fetching or processing contacts: {e}")
    
    # Fetch and process calendar events for the last year
    try:  
        print("Fetching calendar events...")
        calendar_data = get_calendar_events(creds)
        # logging.debug(f"Raw calendar data: {calendar_data}")  
        calendar_df = process_to_dataframe(calendar_data, 'calendar')
        print("Calendar events fetched. Saving to CSV...")
        save_to_csv(calendar_df, 'output/calendar_events.csv')
    except Exception as e:
        logging.error(f"An error occurred while fetching or processing calendar events: {e}")

    # Fetch and process emails for the last month
    try:  
        print("Fetching emails...")
        email_data = get_emails(creds)
        # logging.debug(f"Raw email data: {email_data}")  
        email_df = process_to_dataframe(email_data, 'emails')
        print("Emails fetched. Saving to CSV...")
        save_to_csv(email_df, 'output/emails.csv')
    except Exception as e:
        logging.error(f"An error occurred while fetching or processing emails: {e}")


if __name__ == "__main__":
    main()