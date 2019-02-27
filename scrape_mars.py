from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/webdrivers/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # PART ONE -- IMAGE OF MARS
    # Visit the NASA website to find the top mars image
    jpl_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    jpl_image_url_base = "https://www.jpl.nasa.gov"
    browser.visit(jpl_image_url)
    time.sleep(2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    # Scrape page into Soup
    html_image_site = browser.html
    time.sleep(2)
    mars_image_soup = bs(html_image_site,"html.parser")
    # Find the image in soup
    search_image = mars_image_soup.find(class_="main_image")
    featured_image_url = jpl_image_url_base + search_image["src"]

    # PART TWO -- MARS WEATHER INFORMATION
    # Visit the Twitter website to find the weather information
    tweet_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(tweet_weather_url)
    time.sleep(2)
    # Scrape page into Soup
    html_weather_twitter = browser.html
    time.sleep(2)
    weather_soup = bs(html_weather_twitter,"html.parser")
    # Find the text in soup
    mars_weather = weather_soup.find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # XXXXXXX

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    avg_temps = soup.find('div', id='weather')

    # Get the min avg temp
    min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    mars_data = {
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
