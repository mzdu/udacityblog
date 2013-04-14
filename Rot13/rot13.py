# Unfinished! 
# Should use Jinja2 + Python

import webapp2
import cgi

form = '''
<form method="POST">
    Rot 13.com <br />
    <label>Your text here
        <input type="text" name="text1" value ="%s" size="30"/>
    </label>
    
    <br />

<input type = "submit">      
</form>
'''
 
def escape_html(s):
    return cgi.escape(s, quote=True)
    
class Rot13Page(webapp2.RequestHandler):
    def write_form(self, t1=""):
        self.response.out.write(form % t1)    
    
    def get(self):
        self.write_form()

    def post(self):
        t1 = escape_html(self.request.get('text1'))
        if t1 and t1.isdigit():
            t1 = int(t1)
            t1 = t1 + 13
        
        self.response.out.write(form % t1)    
        
class ThanksPage(webapp2.RequestHandler):
    def get(self):        
        self.response.out.write('thanks.')
        
app = webapp2.WSGIApplication([('/', Rot13Page),
                               ('/thanks', ThanksPage)],
                              debug=True)