# Mission to Mars
## Summary
* A homework assignment for UC Berkeley's Data Analytics Bootcamp
* The project scrapes the following data from the web:
    1. The most recent article title and headline text from this site:
        * https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
    2. The current Featured Image from this site:
        * https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    3. Mars weather information from this site:
        * https://twitter.com/marswxreport?lang=en
    4. A table of Mars facts from this site:
        * https://space-facts.com/mars/
    5. Four images and titles; one for each of Mars' hemispheres from this site:
        * https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
* The project scrapes the data in a Python Jupyter Notebook
* The project also scrapes the data in a Flask app and displays all the information using HTML
### Files
* The analysis includes the following files:
    * A "mission_to_mars.ipynb" Jupyter Notebook that shows the desired information scraped line-by-line
    * An "app.py" Python Flask app that pulls all the information together using these files:
        * A "scrape_mars.py" Python file that scrapes the information (in a similar way that the Jupyter Notebook does)
        * An "index.html" HTML file in the "templates" folder that displays the scraped information in a web page
        * A "style.css" CSS file that formats the HTML file
    * Four PNG screenshots in the "web page screenshots" folder that show images of the final web page
        
    
