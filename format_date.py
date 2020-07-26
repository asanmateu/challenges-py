from datetime import datetime

def format_date(date):
    """ Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM """

    return datetime.strptime(date, '%m/%d/%Y').strftime('%Y%d%m')

print(format_date('11/12/2019'))
