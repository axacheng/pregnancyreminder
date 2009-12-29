#coding=utf-8

import db_model

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class AddInfo(webapp.RequestHandler):
    def get(self):
        pregnancy_handler = db_model.PregnancyGadget(weekday=int(2),
                                                     description=u"""雙胞胎媽媽要比一般單胞胎媽媽來的辛苦，但是恭喜妳呀~! 雙胞胎媽媽盡量要多休息平躺在床上，這樣寶貝才會健康唷！ 前期是胚胎穩定期，所以要格外小心，反正就要按分一點。 中期可以活動就可稍稍活動自如，可是走動也不可太平繁，大概10~20分鐘，就要休息。 後期是關鍵期，決定小孩的出生時間，盡量也是多休息，太過於勞動會讓小孩子提早出生。 1.多胞胎難免會有一大一小的問題產生，心跳也是，不要差異太多就可囉，順其自然，不用太擔心。 2.多胞胎好像真的很容易動到胎氣而出血，所以飲食及行動+家裡的東西最好不要亂動，以免動到胎氣。 PS.參考我同事雙胞胎的經驗，他目前35週，寶寶健康狀況良好，而且大小都跟我單胞胎一樣大唷！""",)
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
