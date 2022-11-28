import gspread
import pandas as pd
import os
import smtplib
import ssl
from email.message import EmailMessage


"""These credentials must be changed to align with TechStars credentials"""
credentials = {
    "installed": {
        "client_id": "323721559700-dqboieeedhqebgdoqnpde2hotvpk3md8.apps.googleusercontent.com",
        "project_id": "esoteric-life-364115",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost/"]
    }
}


def connect():
    """Function that connects to Google Sheets using client email"""
    gc, authorized_user = gspread.oauth_from_dict(credentials)
    sh = gc.create("csv spreadsheet")
    print("Connected to Google Sheets")
    return sh


def create(sh):
    """Function that gets the data from Phantom CSV and uploads the first records in Google Sheets"""
    df = pd.read_csv("https://cache1.phantombooster.com/hrxWS8qGcnE/Am4ee5XhTF9rr7UaMy0P2Q/result.csv")
    aux_df = pd.DataFrame(['**END_OF_RECORDS**'], columns=[df.columns.values[0]])
    df = pd.concat([df, aux_df])
    df_cols = [col for col in df.columns]
    for colum in df_cols:
        if df[f"{colum}"].str.contains('media-exp1').any():
            df['image'] = df[f"{colum}"]
            df = df.fillna('')
    df['image'] = df['image'].apply(lambda path: f'=IMAGE("{path}",4,100,100)'.strip())
    df = df.fillna('')
    sh.sheet1.update([df.columns.values.tolist()] + df.values.tolist(), raw=False)
    print("Records uploaded in Google Sheets")
    return sh


def update(sh):
    """Function that uploads the new records"""
    cell = sh.sheet1.find('**END_OF_RECORDS**', in_column=0)
    csv_url = os.getenv('PHANTOM_CSV')
    print("Getting records from CSV")
    df = pd.read_csv(csv_url, skiprows=cell.row - 2)
    print("Got records from CSV")

    if df.values.size > 0:
        aux_df = pd.DataFrame(['**END_OF_RECORDS**'], columns=[df.columns.values[0]])
        df = pd.concat([df, aux_df])
        df_cols = [col for col in df.columns]
        for colum in df_cols:
            if df[f"{colum}"].str.contains('media-exp1').any():
                df['image'] = df[f"{colum}"]
                df = df.fillna('')
        df['image'] = df['image'].apply(lambda path: f'=IMAGE("{path}",4,100,100)'.strip())
        df = df.fillna('')
        sh.sheet1.update([df.columns.values.tolist()] + df.values.tolist(), raw=False)
        df = df.fillna('')
        sh.sheet1.delete_rows(cell.row)
        sh.sheet1.append_rows(df.values.tolist())
        print("Records updated in Google Sheets")
    else:
        print("No records to update")


"""This function requires the 3D authentication to be activated in the client email"""
# def send_email():
#     sender_email = ""
#     sender_password = ""
#     rec_email = ""
#     subject = ""
#     message = ""
#     em = EmailMessage()
#     em['From'] = sender_email
#     em['To'] = rec_email
#     em['Subject'] = subject
#     em.set_content(message)
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(sender_email, sender_password)
#         smtp.sendmail(sender_email, rec_email, em.as_string())
#
#     print('Email Sent')


def start_connection():
    sh = connect()
    cell = sh.sheet1.find('**END_OF_RECORDS**', in_column=0)
    if cell is None:
        create(sh)
    else:
        update(sh)

