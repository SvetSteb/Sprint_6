from datetime import datetime, timedelta

def tomorrow_date():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    formatted_date = tomorrow.strftime('%d.%m.%Y')
    return formatted_date
