#This module contain all the data related to date and time
from datetime import datetime, date

class Dates_data:

    def get_exp_months(start_date):
        # Get the current date
        current_date = datetime.today()
    
        # Calculate the difference in years and months
        diff_years = current_date.year - start_date.year
        diff_months = current_date.month - start_date.month
    
        # Total experience in months
        exp_months = diff_years * 12 + diff_months
    
        # Handle negative months by adjusting for years
        if diff_months < 0:
            exp_months -= 12
            exp_months += current_date.month - start_date.month + 12
    
        return exp_months
    
    def get_age ():
        # automating age calculation
        birth_date = date(2000, 9, 8)
        current_date = date.today()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

        return int(age)
    
    submit_date = datetime.now()