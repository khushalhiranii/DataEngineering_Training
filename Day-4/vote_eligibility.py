def check_eligibility(age):
    if(age >=18):
        return True
    else:
        return False
age = input("Enter your age:")
try:
    age_int = int(age)
    print(check_eligibility(age_int))
except ValueError:
    print("Invalid age format")