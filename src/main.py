import os
import webapp2
import jinja2
import logging

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape = True)
class Article(db.Model):
    #indicate title is String type
    title = db.StringProperty(required = True)
    #set it to current time
    created = db.DateTimeProperty(auto_now_add = True)
    
    body = db.TextProperty(required = True)

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
        
        self.render(page, articles=articles)
        
        
class AddBlog(Handler):
    def get(self):
        self.render("addBlog.html")
    
    def post(self):
        
        
        self.redirect("/")
        
class MainPage(Handler):
    def get(self):
        self.render("index.html")
#         articles = db.GqlQuery("select * from Articles order by created DESC")
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
                               ('/addblog', AddBlog)], debug=True)