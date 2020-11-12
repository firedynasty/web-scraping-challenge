# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# List of dictionaries
dogs = [{"name": "Fido", "type": "Lab"},
        {"name": "Rex", "type": "Collie"},
        {"name": "Suzzy", "type": "Terrier"},
        {"name": "Tomato", "type": "Retriever"}]


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
def index():

    return render_template("index.html", image_url=image_url)

@app.route("/images")
def second_page_images():

    return render_template("images.html", image_files1=image_files1, image_files2=image_files2, )



if __name__ == "__main__":
    app.run(debug=True)
