from datetime import datetime, timedelta

travel_day = {"l": 45, "h": 55}
full_day = {"l": 75, "h": 85}

def calculate(set):
    total = 0
    current_dt = datetime.strptime(set[0]['start_dt'], '%m/%d/%y').date()

    for pidx, proj in enumerate(set):
        city_tp = proj['city_tp']
        city_tp_last = set[pidx-1]['city_tp']
        start_dt = datetime.strptime(proj['start_dt'], '%m/%d/%y').date()

        # Add gap days between projects to total
        if pidx > 0:
            for day in (current_dt + timedelta(n) for n in range((start_dt - current_dt).days)):
                if city_tp == "l" and city_tp_last == "h":
                    print(f"Adding {travel_day[city_tp_last]} to total cost for {current_dt} as a gap travel day for a {city_tp_last.upper()} cost city.")
                    total += travel_day[city_tp_last]
                else:
                    print(f"Adding {travel_day[city_tp]} to total cost for {current_dt} as a gap travel day for a {city_tp.upper()} cost city.")
                    total += travel_day[city_tp]
        
        end_dt = datetime.strptime(proj['end_dt'], '%m/%d/%y').date()
        num_days = (end_dt - start_dt).days

        for i, day in enumerate(start_dt + timedelta(n) for n in range(num_days + 1)):
            first_day = 0
            last_day = num_days
            if i == first_day or i == last_day:
                # Account for project days that overlap
                if current_dt > day and pidx > 0:
                    print(f"Removing {travel_day[city_tp_last]} from total cost for {day} as a travel day in a {city_tp_last.upper()} cost city.")
                    # Remove day of last project from total
                    total -= travel_day[city_tp_last]
                    # If conflicting rates between projects, use the high cost rate
                    if city_tp == "l" and city_tp_last == "h":
                        print(f"Adding {full_day[city_tp_last]} to total cost for {day} as a full day in a {city_tp_last.upper()} cost city.")
                        total += full_day[city_tp_last]
                    else:
                        print(f"Adding {full_day[city_tp]} to total cost for {day} as a full day in a {city_tp.upper()} cost city.")
                        total += full_day[city_tp]
                else:
                    print(f"Adding {travel_day[city_tp]} to total cost for {day} as a travel day in a {city_tp.upper()} cost city")
                    total += travel_day[city_tp]
            else:
                # Only add day to total if not overlapping
                if current_dt <= day:
                    print(f"Adding {full_day[city_tp]} to total cost for {day} as a full day in a {city_tp.upper()} cost city")
                    total += full_day[city_tp]
                elif pidx > 0:
                    # If conflicting rates between projects, use the high cost rate
                    if city_tp == "h" and city_tp_last == "l":
                        print(f"Removing {full_day[city_tp_last]} from total cost for {day} as a full day in a {city_tp_last.upper()} cost city.")
                        total -= full_day[city_tp_last]
                        print(f"Adding {full_day[city_tp]} to total cost for {day} as a full day in a {city_tp.upper()} cost city.")
                        total += full_day[city_tp]

        current_dt = end_dt + timedelta(days=1)
        
    print(f"Total Reimbursement Cost: {total}")

def get_projects():
    while True:
        try:
            start_dt = input("Enter project START date in format M/D/Y: ")
            check_stdate = datetime.strptime(start_dt, '%m/%d/%y').date()
            break
        except ValueError:
            print("Please enter date in M/D/Y format. Use only the last two digits for the year. Example: 9/1/15")
            continue
    while True:
        try:  
            end_dt = input("Enter project END date in format M/D/Y: ")
            check_endate = datetime.strptime(end_dt, '%m/%d/%y').date()
            if check_stdate > check_endate:
                print("Please enter an end date on or after the previously entered start date.")
                continue
            break
        except ValueError:
            print("Please enter date in M/D/Y format. Use only the last two digits for the year. Example: 9/1/15")
            continue
    while True:
        city_tp = input("High or Low Cost city? (h/l): ")
        if city_tp.lower() not in ['h', 'l']:
            print("Please enter city type as either h or l.")
            continue
        else:
            break
              
    set.append({"start_dt": start_dt, "end_dt": end_dt, "city_tp": city_tp})

    while True:
        more_projects = input("Enter another project in set? (y/n):")
        if more_projects.lower() not in ['y', 'n']:
            print("Please enter either y or n.")
            continue
        else:
            break
    if (more_projects) == "n":
        return
    else:
        get_projects()

if __name__ == "__main__":
    print("Define a Set by entering Projects in chronological order...")
    set = []
    get_projects()
    calculate(set)
    
