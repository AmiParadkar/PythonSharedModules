from datetime import datetime, timedelta


def get_yesterday_date():
    # Get today's date
    today = datetime.today()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    # Format the date as a string
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    return yesterday_str
