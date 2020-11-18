# web-scraping-challenge

## Intro

In this assignment, we are told to build a webscraping flask app that will call information that was scraped from a website about Mars.  The first headline and first paragaph of the news was obtained. An image was obtained for the landing page.  A table of Mars information was obtained using Pandas from a table on their website.  Images of the hemispheres of Mars were obtained.  

## Method

The Library BeautifulSoup was used to scrape the url https://mars.nasa.gov/news/ to obtain the news title and news paragraph that you will find in the image below.  There was a fancy picture that could only be obtained by visiting the second page of https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars so the Library Splinter was used to get the Browser to click to the new page and then Beautiful Soup could obtain the image url.  The Table Mars Facts was obtained from using Pandas' read_html function.  Images of Mars Hemispheres were obtained from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars.

Flask and Pymongo were used in combination to build the two webpages that got the information from above.  Except, the tables and the image_url was preloaded into the html template of the homepage.  A button on the homepage ran Splinter and BeautifulSoup to get the news headline so it would be the latest everytime the button was pressed. A for loop was used in the images page to read off the dictionary of images obtained as described above. 

![Mars_Landing_page](/Missions_to_Mars/Mongo_Flask_App/images/homepage.png)

![Mars_Images](/Missions_to_Mars/Mongo_Flask_App/images/images.png)

## Update

See Directory /Missions_to_mars/Mongo_Flask_App_V2

The same image page gets rendered, however the dictionary was not split into two from the first webscraping exercise(/Missions_to_Mars/mission_to_mars.ipynb)

A nested list is created and then a nested for loop was created to read into a table with two columns.

