from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
import pandas as pd

def init_browser():
	executable_path = {"executable_path": "C:/webdrivers/chromedriver.exe"}
	return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}

    # Retrieve Latest News Article
    mars_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_url)
    time.sleep(5)

	html_mars_site = browser.html
	soup = bs(html_mars_site,"html.parser")

    mars["news_title"] = soup.find("div",class_="content_title").text
	mars["news_p"] = soup.find("div",class_="article_teaser_body").text




    # Retrieve JPL Mars Featured Image
    jpl_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	jpl_image_url_base = "https://www.jpl.nasa.gov"
	browser.visit(jpl_image_url)
	time.sleep(5)
	browser.click_link_by_partial_text('FULL IMAGE')
	time.sleep(5)
	browser.click_link_by_partial_text('more info')
	time.sleep(5)
	html_image_site = browser.html
	mars_image_soup = bs(html_image_site,"html.parser")

	search_image = mars_image_soup.find(class_="main_image")
	mars["featured_image"] = jpl_image_url_base + search_image["src"]






    # Retrieve Mars Weather
	tweet_weather_url = "https://twitter.com/marswxreport?lang=en"
	browser.visit(tweet_weather_url)
	time.sleep(5)

    html_weather_twitter = browser.html
	time.sleep(5)
	weather_soup = bs(html_weather_twitter,"html.parser")
	time.sleep(5)

	mars["weather"] = weather_soup.find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    



    # Retrieve Mars facts
    mars_facts_url = "https://space-facts.com/mars/"
	mars_facts = pd.read_html(mars_facts_url)
	facts_df = mars_facts[0]
	facts_df.columns = ['Description','Value']
	table = facts_df.to_html(header=False, index=False)
	table = table.replace("\n","")
	mars["facts"] = table
	browser.quit()

    # Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
        hemisphere = {}

        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item")[i].click()

        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']

        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text

        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)

        # Finally, we navigate backwards
        browser.back()
        time.sleep(1)

    # Set hemispheres
    mars["hemispheres"] = hemisphere_image_urls

    df = pd.read_html('http://space-facts.com/mars/')[0]
    df.columns = ['description', 'value']
    df.set_index('description', inplace=True)

    table = df.to_html()
    table = table.replace('\n', '')

    mars['facts'] = table

    browser.quit()

    return mars