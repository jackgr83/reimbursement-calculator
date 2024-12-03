from datetime import datetime, timedelta

travel_day = {"l": 45, "h": 55}
full_day = {"l": 75, "h": 85}

def calculate(set):
    total = 0

    current_dt = datetime.strptime(set[0]['start_dt'], '%m/%d/%y').date()

    for proj in set:
        city_tp = proj['city_tp']
        start_dt = datetime.strptime(proj['start_dt'], '%m/%d/%y').date()

        # Add gap days between projects to total
        for day in (current_dt + timedelta(n) for n in range((start_dt - current_dt).days)):
            print(f"Adding {current_dt} to total cost as a travel day in between projects")
            total += travel_day[city_tp]
        
        end_dt = datetime.strptime(proj['end_dt'], '%m/%d/%y').date()
        num_days = (end_dt - start_dt).days

        for i, day in enumerate(start_dt + timedelta(n) for n in range(num_days + 1)):
            first_day = 0
            last_day = num_days


            if i == first_day or i == last_day:
                # Account for project days that overlap
                if current_dt > day:
                    print(f"Removing {day} as a travel day and replacing it with a full day since it overlaps with last project")
                    total -= travel_day[city_tp]
                    total += full_day[city_tp]
                else:
                    print(f"Adding {day} to total cost as a travel day")
                    total += travel_day[city_tp]
            else:
                # Only add day to total if not overlapping
                if current_dt < day:
                    print(f"Adding {day} to total cost as a full day")
                    total += full_day[city_tp]
        current_dt = end_dt + timedelta(days=1)
    print(f"Total Reimbursement Cost: {total}")

def get_projects():  
    start_dt = input("Enter project start date in format M/D/Y: ")
    end_dt = input("Enter project end date in format M/D/Y: ")
    city_tp = input("High or Low Cost city? (h/l): ")
    set.append({"start_dt": start_dt, "end_dt": end_dt, "city_tp": city_tp})
    if (input("Enter another project in set? (y/n):")) == "n":
        return
    else:
        get_projects()

if __name__ == "__main__":
    print("Define a Set by entering Projects in chronological order...")
    set = []
    get_projects()

    calculate(set)
    
