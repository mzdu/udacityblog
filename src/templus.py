import os
import webapp2
import jinja2
import logging
import datamodel

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape = True)


class Handler(webapp2.RequestHandler):
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **values):
        self.write(self.render_str(template, **values))    
         
# class AddBlog(Handler):
#     def get(self):
#         self.render("/addBlog.html")
#     
#     def post(self):
#         #get(name from html page)
#         ti1 = self.request.get("title")
#         art1 = self.request.get("article")
# 
#         if ti1 and art1:
#             #title and body are keys from Article(db.Model)  title, body
#             a = Article(title=ti1, body=art1)
#             a.put()
#             logging.info("injection successful")
#             self.redirect("/")
#         
#         else:
#             errmsg = "error, one of these texts need to be filled."
#             self.render("/addBlog.html", title1=ti1, article1=art1, error=errmsg)
#         
class MainPage(Handler):
    def get(self):
        
        
        
        
        articles = db.GqlQuery("select * from Article order by created DESC")
        self.render("index.html", Articles = articles)
    
        
        
        
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
    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)