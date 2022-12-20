from datetime import datetime
import gspread
import os


def connect():
    """Function that connects to Google Sheets"""
    gc = gspread.service_account(filename="/Users/yazmingiraldo/Documents/phantomData/credentials.json")
    sh = gc.open_by_url(os.getenv('SHEETS_URL'))
    print("Connected to Google Sheets")
    return sh


def create(sh):
    """Function that gets the data from Phantom CSV and uploads the first records in Google Sheets"""
    search_url = f"{os.getenv('SEARCH_URL')}?date={datetime.now().date()}"

    sh.sheet1.append_row([search_url])
    print("Record uploaded in Google Sheets")


if __name__ == '__main__':
    sh = connect()
    create(sh)