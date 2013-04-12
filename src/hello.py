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

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("That is a valid day.")
     
 
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)
        

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)