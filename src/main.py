# -*- coding: utf-8 -*-

import db_model

from django.utils import simplejson
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext.webapp.util import run_wsgi_app


class Init(webapp.RequestHandler):
  """ Create first entry to db_model.PregnancyGadget """
  
  def get(self):
    query = db_model.PregnancyGadget.get_by_key_name('preg')
    if query is None:
      query = db_model.PregnancyGadget(key_name='preg', 
                                       weekday=0, 
                                       description="""This record is generated 
                                                   by initial class""")
      query.put()
      self.response.out.write('Initial done')
      

class PostInfo(webapp.RequestHandler):
  """ Post description to db_model.PregnancyGadget db.
  
  The user need to user Goolge account to login page then should be able to 
  update data into db_model.PregnancyGadget"""
  def get(self):
    query = db_model.PregnancyGadget.all()
    query.order('-weekday')
    
    if query is None:
      self.response.out.write('Please run /init first')
    else:
      self.response.out.write(template.render('ui/post.html', 
                                             {'query_from_preg': query}))
    
  def post(self):
    user_login = users.get_current_user()
    if user_login:
      weekday = self.request.get('weekday')
      description = self.request.get('description')
      try:
        commit_db = db_model.PregnancyGadget(weekday=int(weekday), 
                                             description=description)
        #import sys
        #print >> sys.stderr, type(description)
        commit_db.put()
        self.redirect('/add')
      except ValueError:
        self.response.out.write("""Error occur during update db...""")
    else:
      self.redirect(users.create_login_url(self.request.uri))
    
    
class EditPost(webapp.RequestHandler):
  """ User can edit exist data description by weekday """
  @login_required
  def get(self, weekday):
    query = db_model.PregnancyGadget.all()
    query.filter('weekday =', int(weekday))
    self.response.out.write(template.render('ui/edit.html', {'query': query}))
  
  def post(self, weekday):
    key = self.request.get('key')
    query = db_model.PregnancyGadget.get(key)
    query.description = self.request.get('description')
    query.put()
    self.redirect('/add')
       

    
class ListPost(webapp.RequestHandler):
  """ Show result from db_model.PregnancyGadget then covert to JSON object 
  
  We fetch the description from datastore per your weekday integer 
  and use simplejson.dumps convert context to json object.  
  JSON object. 
  """
  db_model.PregnancyGadget.all() ### TODO, we cannot remove this line otherwise db_model cannot be initialed.
  def get(self, weekday):
    response = []
    query = db_model.PregnancyGadget.all()
    query.filter('weekday =', int(weekday))
    
    for result in query:
      response.append({weekday: result.description})
    self.response.out.write(simplejson.dumps(response))
     
                      
class Cal(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('ui/cal.html', {}))

def main():
    app = webapp.WSGIApplication([
                                  ('/init', Init),
                                  ('/add', PostInfo), 
                                  ('/edit/(\d+)', EditPost),
                                  ('/(\d+)', ListPost),
                                  ('/c', Cal)], debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
