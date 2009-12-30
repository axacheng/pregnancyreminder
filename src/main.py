#coding=utf-8

import db_model

from django.utils import simplejson
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app



class PostInfo(webapp.RequestHandler):
  """ Post description to db_model.PregnancyGadget db.
  
  The user need to user Goolge account to login page then should be able to 
  update data into db_model.PregnancyGadget"""
  
  def get(self):
    fetch_list = db_model.PregnancyGadget.get_by_key_name('weekday')
    if fetch_list is None:
      self.response.out.write('There is nothing on your PregnancyGadget db')
    else:
      self.response.out.write(template.render('ui/post.html', 
                                              {'weekday': weekday, 
                                               'description': description}))
    
  def post(self):
    user_login = users.get_current_user()
    if user_login:
      weekday = self.request.get('weekday')
      description = self.request.get('description')
      try:
        commit_db = db_model.PregnancyGadget(weekday=weekday, 
                                             description=description)
        commit_db.put()
        self.redirect('/post')
      except BadValueError:
        self.response.out.write("""Error occur during update db...""")
    else:
      self.redirect(users.create_login_url(self.request.uri))
    
    
class MainPage(webapp.RequestHandler):
  """ Show result from db_model.PregnancyGadget then covert to JSON object 
  
  We only fetch 50 records at the time and use simplejson convert context to 
  JSON object. 
  """
  def get(self, page_number):
    query = db_model.PregnancyGadget.all()
    #print 'count: %s <br>' % query.filter("weekday =", int(page_number)).count()
    query.filter('weekday =', int(page_number))
    mesg = query.fetch(50, 0)
    if len(mesg) == 0:
      print 'weekday is invalid'
    else:
      self.response.out.write(simplejson.dumps(mesg))  
      #self.response.out.write('key: %s <br> value: %s <br>' % (
      #                        result.weekday,
      #                        result.description))
                      
def main():
    app = webapp.WSGIApplication([
                                  ('/(\d+)', MainPage),
                                  ('/add', PostInfo), ], debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
