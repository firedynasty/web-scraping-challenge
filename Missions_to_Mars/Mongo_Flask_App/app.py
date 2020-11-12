# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_news

# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


image_url = {'url':'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18182_ip.jpg'}

image_files1 = [{'title': 'Valles Marineris',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'},
 {'title': 'Cerberus Hemisphere',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}]

image_files2 = [{'title': 'Schiaparelli Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
 {'title': 'Syrtis Major',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}]


# create route that renders index.html template
@app.route("/")
def home():

    news_info = mongo.db.collection.find_one()

    return render_template("index.html", image_url=image_url, news_info=news_info)


@app.route("/scrape")
def scrape():
	news_data = scrape_news.scrape_info()

	mongo.db.collection.update({}, news_data, upsert=True)

	return redirect("/")

@app.route("/images")
def second_page_images():

    return render_template("images.html", image_files1=image_files1, image_files2=image_files2, )



if __name__ == "__main__":
    app.run(debug=True)
