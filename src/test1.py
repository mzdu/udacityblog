import webapp2

class TestPage(webapp2.RequestHandler):
    
    def write_sth(self):
        self.response.out.write("Thanks for coming!")

    def get(self):
        self.write_form()



app = webapp2.WSGIApplication([('/', TestPage)],
                              debug=True)