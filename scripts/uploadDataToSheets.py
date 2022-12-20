import gspread
import pandas as pd
import os


def connect():
    """Function that connects to Google Sheets"""
    gc = gspread.service_account(filename="phantomData/credentials.json")
    sh = gc.open_by_url(os.getenv('SHEETS_URL'))
    print("Connected to Google Sheets")
    return sh


def create(sh):
    """Function that gets the data from Phantom CSV and uploads the first records in Google Sheets"""
    df = pd.read_csv("https://cache1.phantombooster.com/hrxWS8qGcnE/Am4ee5XhTF9rr7UaMy0P2Q/result.csv")
    aux_df = pd.DataFrame(['**END_OF_RECORDS**'], columns=[df.columns.values[0]])
    df = pd.concat([df, aux_df])
    df_cols = [col for col in df.columns]
    for colum in df_cols:
        if df[f"{colum}"].str.contains('static-exp1').any():
            df['image'] = df[f"{colum}"]
            df = df.fillna('')
    df['image'] = df['image'].apply(lambda path: f'=IMAGE("{path}",4,100,100)'.strip())
    df = df.fillna('')
    sh.sheet1.update([df.columns.values.tolist()] + df.values.tolist(), raw=False)
    print("Records uploaded in Google Sheets")


def update(sh, cell):
    """Function that uploads the new records"""
    csv_url = os.getenv('PHANTOM_CSV')
    print("Getting records from CSV")
    df = pd.read_csv(csv_url, skiprows=cell.row - 2)
    print("Got records from CSV")

    if df.values.size > 0:
        aux_df = pd.DataFrame(['**END_OF_RECORDS**'], columns=[df.columns.values[0]])
        df = pd.concat([df, aux_df])
        df_cols = [col for col in df.columns]
        for colum in df_cols:
            if df[f"{colum}"].str.contains('static-exp1').any():
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


def start_connection():
    sh = connect()
    cell = sh.sheet1.find('**END_OF_RECORDS**', in_column=0)
    if cell is None:
        create(sh)
    else:
        update(sh, cell)
