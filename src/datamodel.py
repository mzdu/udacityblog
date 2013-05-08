from google.appengine.ext import db

class Article(db.Model):
    body = db.TextProperty()
    keywords = db.StringListProperty()
    