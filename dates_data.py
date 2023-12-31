#This module contain all the data related to date and time
from datetime import datetime, date

class Dates_data:

    def get_exp_months ():
        #defining experience months
        current_date = datetime.today()
        current_month = current_date.month
        exp_months = 9
        exp_months += current_month-7

        return int(exp_months)
    
    def get_age ():
        # automating age calculation
        birth_date = date(2000, 9, 8)
        current_date = date.today()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

        return int(age)
    
    submit_date = datetime.now()