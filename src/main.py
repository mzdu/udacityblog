import os
import webapp2
import jinja2
import logging

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape = True)



class Article(db.Model):
    #if one of these required=True propery fail to input, the whole transaction will not be injected into datastore
    #indicate title is String type
    
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    #set it to current time
    created = db.DateTimeProperty(auto_now_add = True)


class Handler(webapp2.RequestHandler):
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))    
    
    def render_page(self, articles=""):
#         arts = db.GqlQuery("select * from Art order by created DESC")
#         self.render("index.html", title1=title, art1=art, error1=error, arts1=arts)
        pass
#         self.render(page, articles=articles)

        
class AddBlog(Handler):
    def get(self):
        self.render("/addBlog.html",title1='start your title here', article1='arti', error='err111')
    
    def post(self):
        #get(name from html page)
        ti1 = self.request.get("title")
        art1 = self.request.get("article")

        if ti1 and art1:
            #title and body are keys from Article(db.Model)  title, body
            a = Article(title=ti1, body=art1)
            a.put()
            logging.info("injection successful")
            self.redirect("/success")
        
        else:
            errmsg = "error, one of these texts need to be filled."
            self.render("/addBlog.html", title1=ti1, article1=art1, error=errmsg)


class SuccessHandler(Handler):
    def get(self):
        self.render("success.html")
        
    def post(self):
        self.redirect("/")
        
class MainPage(Handler):
    def get(self):
        articles = db.GqlQuery("select * from Article order by created DESC")
        self.render("index.html", Articles = articles)
        
        
        #setup cookies
        visits = self.request.cookies.get('visits', '0')
        visits = int(visits) + 1
        self.response.headers.add_header('Set-cookie', 'visits=%s' % visits)
        self.write("you have been here %s times." % visits)
        # CRC32 - checksums, fast to prevent cookies from modification
        # MD5 - fast, secure kind of, for limited input
        # SHA1 - secure
        # SHA256 - pretty good, but slower
        '''
        import hashlib
        hashlib.md5("hello").hexdigit()
        ==> '23u2839280380023...'
        '''
        
        
        
        
#         self.render_page("index.html", articles = articles)         
    def post(self):
        self.write("this is a post main page")
#         title2 = self.request.get("title1")
#         art2 = self.request.get("art1")
#         
#         if title2 and art2:
#             a = Article(title=title2,art=art2)
#             a.put()
#             self.redirect('/')
#         else:
#             error2 = "Sorry Error."
#             
#             self.render_page(title2, art2, error2)
    
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/addblog', AddBlog),
                               ('/success', SuccessHandler)], debug=True)