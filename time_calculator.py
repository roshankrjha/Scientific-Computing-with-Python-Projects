def get_days_later(days):
    if days == 1:
        return "(Next Day)"
    elif days > 1:
        return f"({days} Days Later)"
    else:
        return ""

def add_time(start, duration, day=False):
    week_days =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
    ]
    # Get the hours, minutes and period
    days_later = 0
    one_day = 24
    half_day = 12

    sh, sm = start.split(':')
    sm, period = sm.split()
    dh, dm = duration.split(':')

    # Get Clean Data 
    start_hours = int(sh)
    start_mins = int(sm)
    duration_hours = int(dh)
    duration_mins = int(dm)
    period = period.strip().lower()

    # Get Total hours and minutes
    total_hours = start_hours + duration_hours
    total_mins = start_mins + duration_mins

    # Shift Minuts to hours if its more than 60
    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if dh or dm:
        if period == 'pm' and total_hours > half_day:
            if total_hours % one_day >= 1.0:
                days_later += 1

        if total_hours >= half_day:
            hours_left = total_hours / one_day
            days_later += int(hours_left)

        tth = total_hours
        while True:
            if tth < half_day:
                break
                
            if tth >= half_day:
                if period == 'am':
                    period = 'pm'
                elif period == 'pm':
                    period = 'am'
                tth -= half_day
    
    remaning_hours = int(total_hours % half_day) or start_hours + 1
    remaning_mins = int(total_mins % 60)

    results = f'{remaning_hours}:{remaning_mins:02} {period.upper()}'
    if day:
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f' {current_day.title()} {get_days_later(days_later)}'
    else:
        results = " ".join((results, get_days_later(days_later)))
    return results               

# =====================================================================================
# Returns: 6:10 PM
print(add_time("3:00 PM", "3:10"))
# Returns: 2:02 PM, Monday
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 12:03 PM
print(add_time("11:43 AM", "00:20"))
# Returns: 1:40 AM (next day)
print(add_time("10:10 PM", "3:30"))
# Returns: 12:03 AM, Thursday (2 days later)
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 7:42 AM (9 days later)
print(add_time("6:30 PM", "205:12"))
# =====================================================================================