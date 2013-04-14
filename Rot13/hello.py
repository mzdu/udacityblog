import webapp2

form = '''
<form method="POST">
    What is your birthday? <br />
    <label>Month
        <input type="text" name="month" value=%(month)s />
    </label>
    <label>Date
        <input type="text" name="date" value=%(day)s />
    </label>
    <label>Year
    <input type="text" name="year" value=%(year)s />
    </label>
    
    <br />
    <div style="color: red">%(error123)s</div>
    <br />
    
<input type = "submit">      
</form>
'''


def valid_month(month):
    if month and month.isdigit():
        month = int(month)
        if month >= 1 and month <= 12:
            return month

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day >= 1 and day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That is a valid submit!")

class MainPage(webapp2.RequestHandler):
    
    def write_form(self, error="", month="1", day="1", year="2013"):
        self.response.out.write(form % {"error123": error,
                                        "month": month,
                                        "day": day,
                                        "year": year})

    def get(self):
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_month(self.request.get('date'))
        user_year = valid_year(self.request.get('year'))
        
        if not (user_month and user_day and user_year):
            self.write_form("not valid")
        else:
            self.redirect('/thanks')



app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThanksHandler)],
                              debug=True)