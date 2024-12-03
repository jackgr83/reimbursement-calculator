from datetime import datetime, timedelta

travel_day = {"l": 45, "h": 55}
full_day = {"l": 75, "h": 85}

def calculate(set):
    print(set)
    total = 0
    for proj in set:
        start_dt = datetime.strptime(proj['start_dt'], '%m/%d/%y').date()
        end_dt = datetime.strptime(proj['end_dt'], '%m/%d/%y').date()
        city_tp = proj['city_tp']
        num_days = (end_dt - start_dt).days
        for i, day in enumerate(start_dt + timedelta(n) for n in range(num_days + 1)):
            first_day = 0
            last_day = num_days

            if i == first_day:
                total += travel_day[city_tp]
            elif i == last_day:
                total += travel_day[city_tp]
            else:
                total += full_day[city_tp]
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
    print("Define a set...")
    set = []
    get_projects()

    calculate(set)
    
