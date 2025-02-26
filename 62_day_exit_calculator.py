from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate the 62nd day from today
exit_date = today + timedelta(days=62)

# Format the date
formatted_exit_date = exit_date.strftime("%A, %d %B %Y")

# Display the result
print(f"The 62nd day from today is: {formatted_exit_date}")
