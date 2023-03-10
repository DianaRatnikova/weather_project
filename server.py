from python_org_news import get_python_news
from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def index():
    page_title = "Новости Python"
    weather = weather_by_city("Moscow, Russia")
    news_list = get_python_news()
  #  if weather:
 #       weather_text =  f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
 #   else:
  #      weather_text =   "Сервис погоды временно недоступен"
    return render_template("index.html", weather=weather, page_title=page_title, news_list = news_list)


if __name__=="__main__":
    app.run(debug = True)