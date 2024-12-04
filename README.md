# Travel Reimbursement Calculator

### Introduction
This code calculates the total travel reimbursement amount for a given set of projects. A project contains a start date, end date, and a type of city based on cost of living (high vs low). A set can contain one or multiple projects.

The reimbursement calculator abides by the following rules:
- First day and last day of a project, or sequence of projects, is a travel day.
- Any day in the middle of a project, or sequence of projects, is considered a full day.
- If there is a gap between projects, then the days on either side of that gap are travel days.
- If two projects push up against each other, or overlap, then those days are full days as well.
- Any given day is only ever counted once, even if two projects are on the same day.
- A travel day is reimbursed at a rate of 45 dollars per day in a low cost city.
- A travel day is reimbursed at a rate of 55 dollars per day in a high cost city.
- A full day is reimbursed at a rate of 75 dollars per day in a low cost city.
- A full day is reimbursed at a rate of 85 dollars per day in a high cost city.

### Requirements
A working installation of Python 3.x

### Instructions
Follow these steps to use the reimbursement calculator:

1. Clone this repository locally:
```
git clone https://github.com/jackgr83/reimbursement-calculator.git
```

2. Navigate to the project root directory:
```
cd ./reimbursement-calculator
```

3. Run the reimbursement calculator via python:
```
python calculate.py
```

4. Follow the prompts to define a set. Enter a project or multiple projects. Each project must contain a start date and end date in month/day/year format with the year abbreviated to the last two digits (e.g. 9/1/15), and a city type. After entering in the last project, responding no at the last prompt will automatically run the reimbursement calculator on the data provided. The calculator will output the amount of reimbursement for each date and the total reimbursement amount.