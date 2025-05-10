import re
import datetime

def roundoff_year(today, birth_date):
    if((today.month, today.day) < (birth_date.month, birth_date.day)):
        return 1
    else:
        return 0

def calculate_age(birthdate):
    birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.datetime.today()

    age = today.year - birth_date.year - (roundoff_year(today, birth_date))
    return f"Your age is {age} years"


def validate_dob(birthdate):
    pattern = re.compile(r'(19[0-9]{2}|20[0-1][0-9]|202[0-5])-(0[1-9]|1[0-2])-(0[1-9]|[12][1-9]|3[0|1])')
    match = pattern.match(birthdate)
    
    if not match:
        return "Invalid Format"
    
    else:
        return calculate_age(birthdate)

print(validate_dob('2024-07-25'))