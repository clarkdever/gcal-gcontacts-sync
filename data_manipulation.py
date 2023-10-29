import pandas as pd
import logging

def diff_invitees_contacts(calendar_df, contacts_df):
    logging.debug("Starting diff_invitees_contacts function.")
    logging.debug(f"Calendar DataFrame head: {calendar_df.head()}")
    logging.debug(f"Contacts DataFrame head: {contacts_df.head()}")
    
    # Assume 'email' columns in both DataFrames
    non_contacts = calendar_df[~calendar_df['email'].isin(contacts_df['email'])]
    logging.debug(f"Non-contacts DataFrame head: {non_contacts.head()}")
    
    return non_contacts[['email', 'meeting_title']]

def compare_emails_to_contacts(email_df, contacts_df):
    logging.debug("Starting compare_emails_to_contacts function.")
    logging.debug(f"Email DataFrame head: {email_df.head()}")
    logging.debug(f"Contacts DataFrame head: {contacts_df.head()}")
    
    email_count_from_contacts = email_df[email_df['sender'].isin(contacts_df['email'])].count()
    email_count_from_non_contacts = email_df[~email_df['sender'].isin(contacts_df['email'])].count()
    
    logging.debug(f"Email count from contacts: {email_count_from_contacts}")
    logging.debug(f"Email count from non-contacts: {email_count_from_non_contacts}")

    return email_count_from_contacts, email_count_from_non_contacts