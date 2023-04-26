from webapp.python_org_news import get_python_news_without_database #можно убрать
from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.models import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
      page_title = "Новости Python"
      weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
      news_list = get_python_news_without_database() #старый вариант - парсинг с сайта
      news_list = News.query.order_by(News.published.desc()).all() # добавление из базы данных с сортировкой по дате

      #  if weather:
    #       weather_text =  f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    #   else:
      #      weather_text =   "Сервис погоды временно недоступен"
      return render_template("index.html", weather=weather, page_title=page_title, news_list = news_list)

    return app


if __name__=="__main__":
  app.run(debug = True)