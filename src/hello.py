import webapp2

form = '''
<form method="POST">
    What is your birthday? <br />
    <label>Month
        <input type="text" name="month" />
    </label>
    <label>Date
        <input type="text" name="date" />
    </label>
    <label>Year
    <input type="text" name="year" />
    </label>
<input type = "submit">      
</form>
'''


class MainPage(webapp2.RequestHandler):
    from valid-day import valid_day
    from validatemonth2 import valid_month
    from valid-year import valid_year
    

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))
        
        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Correct!")
        
        
 

        

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)