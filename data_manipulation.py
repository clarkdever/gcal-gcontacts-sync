import pandas as pd

#data_manipulation.py

def diff_invitees_contacts(calendar_df, contacts_df):
    # Assume 'email' columns in both DataFrames
    non_contacts = calendar_df[~calendar_df['email'].isin(contacts_df['email'])]
    return non_contacts[['email', 'meeting_title']]

def compare_emails_to_contacts(email_df, contacts_df):
    email_count_from_contacts = email_df[email_df['sender'].isin(contacts_df['email'])].count()
    email_count_from_non_contacts = email_df[~email_df['sender'].isin(contacts_df['email'])].count()
    return email_count_from_contacts, email_count_from_non_contacts
