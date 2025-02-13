import calendar
import datetime

def generate_working_day_schedule(year, month, filename="schedule.txt"):
    # Determine the number of days in the month
    num_days = calendar.monthrange(year, month)[1]
    
    # Define a dash line (using 128 dashes similar to your example)
    dash_line = '-' * 175
    
    with open(filename, 'w') as file:
        # Loop through each day of the month
        for day in range(1, num_days + 1):
            current_date = datetime.date(year, month, day)
            current_day_name = calendar.day_name[current_date.weekday()]
            # Check if the day is a working day (Monday=0, Tuesday=1, ..., Friday=4)
            if current_date.weekday() < 5:
                # Write the formatted schedule entry for the day
                file.write(dash_line + "\n")
                file.write("\n")
                file.write("Date = " + current_date.strftime("%d-%m-%Y") +"  "  + current_day_name + "\n")
                file.write("To Do:\n")
                file.write("\t1)\n")
                file.write("\n")
                # file.write(dash_line + "\n\n")

if __name__ == "__main__":
    # Example: Create a schedule for February 2025
    year = 2025
    month = 2
    generate_working_day_schedule(year, month, filename="working_days_feb_2025.txt")
    print(f"Schedule for {month:02d}-{year} created in 'working_days_feb_2025.txt'.")


"""
How It Works
    Modules Used:
        calendar is used to get the number of days in the month.
        datetime is used for creating date objects and formatting dates.

    Function generate_working_day_schedule:
        It accepts a year, a month, and an optional filename.
        It loops through all days in the month.
        For each day, it checks if the day is a weekday (Monday to Friday).
        For each working day, it writes a header and the following lines (with a "To Do:" section) into the text file.

    Script Execution:
        The script creates a schedule for February 2025 and saves it as working_days_feb_2025.txt.

Output Like:
...
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Date = 26-02-2025
To Do:
	1)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Date = 27-02-2025
To Do:
	1)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Date = 28-02-2025
To Do:
	1)
 .........
"""
