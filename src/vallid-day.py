def valid_day(day):
#     if day>='1' and day<='31':
#         return day

    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <=31:
            return day

#print valid_day('15')
# valid_day('0') => None    
# valid_day('1') => 1
# valid_day('15') => 15
# valid_day('500') => None