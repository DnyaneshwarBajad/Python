months_to_days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
                  'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
day_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_start_day_of_year(year):
    """Calculate the start day of the year using Zeller's Congruence."""
    day = (year - 1) % 400
    day = (day // 100) * 5 + ((day % 100) - (day % 100) // 4) + ((day % 100) // 4) * 2
    return day % 7

def generate_month_grid(start_day, days_in_month):
    """Generate a 2D grid for the given month."""
    grid = [['' for _ in range(7)] for _ in range(6)]
    current_day = 1

    for i in range(6):
        for j in range(7):
            if i == 0 and j < start_day:
                continue
            if current_day > days_in_month:
                break
            grid[i][j] = f"{current_day:2}"
            current_day += 1

    return grid

def display_month_grid(month_name, year, grid):
    """Display the month grid with headers."""
    output = f"{month_name} {year}".center(20, '-') + '\n'
    output += ' '.join(day_names) + '\n'
    for week in grid:
        output += ' '.join(day if day else '  ' for day in week) + '\n'
    return output

def cal_printer(month, year):
    """Generate a formatted string for a specific month's calendar."""
    days_in_month = months_to_days[list(months_to_days.keys())[month - 1]]
    if month == 2 and is_leap_year(year):
        days_in_month = 29

    start_day = (get_start_day_of_year(year) + sum(
        [months_to_days[list(months_to_days.keys())[i]] for i in range(month - 1)]
    )) % 7

    grid = generate_month_grid(start_day, days_in_month)
    month_name = list(months_to_days.keys())[month - 1]
    return display_month_grid(month_name, year, grid)

def cal_printer_year(year, format_type, fill_char='-'):
    """Generate and print a year's calendar in various formats."""
    month_grids = [cal_printer(i + 1, year).splitlines() for i in range(12)]
    formats = {
        '3X4': [(3, 4)],
        '4X3': [(4, 3)],
        '6X2': [(6, 2)],
        '12X1': [(12, 1)],
        '2X6': [(2, 6)]
    }
    
    if format_type not in formats:
        print("Invalid format type.")
        return

    rows, cols = formats[format_type][0]
    for r in range(rows):
        for i in range(7):  # Print 7 lines of each month block
            row_output = "   ".join(
                month_grids[r * cols + c][i] if r * cols + c < len(month_grids) else " " * 20
                for c in range(cols)
            )
            print(row_output)
        print(fill_char * (21 * cols))

# User interaction
year = int(input("Enter the year: "))
format_type = input("Enter the format (3X4, 4X3, 6X2, 12X1, 2X6): ")
fill_char = input("Enter a filler character (default is '-'): ") or '-'
cal_printer_year(year, format_type, fill_char)
