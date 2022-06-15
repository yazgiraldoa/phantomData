from datetime import datetime
import gspread


def connect():
    """Function that connects to Google Sheets"""
    gc = gspread.service_account(filename="/Users/yazmingiraldo/Documents/phantomData/credentials.json")
    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1LJr7y2TuMiRO7H2-sCo5d8gnrWbMui6CpR9V7-Y46hc/edit?usp=sharing")
    print("Connected to Google Sheets")
    return sh


def create(sh):
    """Function that gets the data from Phantom CSV and uploads the first records in Google Sheets"""
    search_url = "https://www.linkedin.com/sales/search/people?query=(recentSearchParam%3A" + \
                 "(id%3A1700373100%2CdoLogHistory%3Atrue)%2Cfilters%3AList" + \
                 "((type%3ATITLE%2Cvalues%3AList((id%3A103%2Ctext%3ACo-Founder%2CselectionType%3AINCLUDED))" + \
                 "%2CselectedSubFilter%3ACURRENT)%2C(type%3AYEARS_AT_CURRENT_COMPANY%2Cvalues%3AList" + \
                 "((id%3A1%2Ctext%3ALess%2520than%25201%2520year%2CselectionType%3AINCLUDED)))%2C" + \
                 "(type%3AYEARS_IN_CURRENT_POSITION%2Cvalues%3AList((id%3A1%2Ctext%3ALess%2520than%25201" + \
                 "%2520year%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList" + \
                 "((id%3A102394087%2Ctext%3AMiami%252C%2520Florida%252C%2520United%2520States" + \
                 "%2CselectionType%3AINCLUDED)%2C(id%3A90000056%2Ctext%3AMiami-Fort%2520Lauderdale%2520Area" + \
                 f"%2CselectionType%3AINCLUDED)))))&sessionId=2muDqMQ5T9an7KA1TBqzgw%3D%3D?date={datetime.now().date()}"

    sh.sheet1.append_row([search_url])
    print("Record uploaded in Google Sheets")


if __name__ == '__main__':
    sh = connect()
    create(sh)
