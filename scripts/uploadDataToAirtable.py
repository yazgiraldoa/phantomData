import os
from pyairtable import Table
import pandas as pd


def connect_to_airtable():
    """Function that connects to Airtable API"""
    base_id = ''
    api_key = os.getenv('API_KEY')
    table_name = os.getenv('TABLE_NAME')
    base_url = os.getenv('BASE_URL')
    split_url = base_url.split('/')
    try:
        if 'app' in split_url[3]:
            base_id = split_url[3]
    except Exception as e:
        return e.__str__()

    table = Table(api_key, base_id, table_name)
    return table


def create(table):
    """Function that gets the data from Phantom CSV and uploads the first records in Airtable"""
    df = pd.read_csv(os.getenv('PHANTOM_CSV'))
    df = df.fillna('')
    df = df.applymap(str)
    fields = df.to_dict('records')
    table.batch_create(fields, typecast=True)


def update(table, row_count):
    """Function that uploads the new records"""
    csv_url = os.getenv('PHANTOM_CSV')
    df = pd.read_csv(csv_url, header=0, skiprows=range(1, row_count + 1))
    if df.values.size > 0:
        df = df.fillna('')
        df = df.applymap(str)
        fields = df.to_dict('records')
        table.batch_create(fields, typecast=True)
    else:
        print("No records to update")


if __name__ == '__main__':
    table = connect_to_airtable()
    records = table.all()
    row_count = len(records)
    if row_count == 0:
        create(table)
    else:
        update(table, row_count)
