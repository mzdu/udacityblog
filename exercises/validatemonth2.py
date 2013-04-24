# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#



def valid_month(month):
    
    months1 = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
# convert a list to dictionary          
    month_abbvs = dict((m[:3].lower(), m) for m in months1)
    
    
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

    
#print valid_month("jansd")
#print month_abbvs
# valid_month("january") => "January"    
# valid_month("January") => "January"
# valid_month("foo") => None
# valid_month("") => None

