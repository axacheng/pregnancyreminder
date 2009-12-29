#coding=utf-8

import db_model

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class AddInfo(webapp.RequestHandler):
    def get(self):
        pregnancy_handler = db_model.PregnancyGadget(weekday=int(2),
                                                     description=u"""好好好""",)
        pregnancy_handler.put()
        self.response.out.write('Fetch done...')


class MainPage(webapp.RequestHandler):
    def get(self, page_number):
        query = db_model.PregnancyGadget.all()
        #print 'count: %s <br>' % query.filter("weekday =", int(page_number)).count()
        query.filter('weekday =', int(page_number))
        mesg = query.fetch(50, 0)
        if len(mesg) == 0:
            print 'weekday is invalided'
        else:
            for result in mesg:
                self.response.out.write('key: %s <br> value: %s <br>' % (
                                        result.weekday,
                                        result.description))
                #return result.explain, result.weekday
        
        
def main():
    app = webapp.WSGIApplication([
                                  ('/(\d+)', MainPage),
                                  ('/add', AddInfo), ], debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
