from datetime import datetime, timedelta

def days_hours_to_now(input_date):
    input_date = datetime.strptime(input_date, "%Y-%m-%d")
    now = datetime.now()
    time_diff = now - input_date
    days_diff = time_diff.days
    hours_diff = time_diff.seconds // 3600
    return days_diff, hours_diff

input_date = input("Enter a date (YYYY-MM-DD): ")
days, hours = days_hours_to_now(input_date)
print(f"Number of days until now: {days}")
print(f"Number of hours until now: {hours}")
