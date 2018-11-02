from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

#NASA Mars News
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find('div',class_='content_title').text
    news_p = soup.find("div", class_='article_teaser_body').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    
#JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.find_by_id('full_image').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('img', class_ = 'fancybox-image')['src'] 
    mars_data['featured_image_url'] = featured_image_url

#Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_data['mars_weather'] = mars_weather

#Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df_mars = tables[0]
    df_mars.columns = ['Description', 'Value']
    html_mars = df_mars.to_html()
    mars_data['html_mars'] = html_mars

#Hemisphere Images
    hemisphere_image_urls = []

#Valles Marineris Hemisphere

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.find_link_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    valles_url = soup.find('div', 'downloads').a['href']
    valles_title = soup.find('h2', class_='title').text
    valles = {
        'title': valles_title,
        'img_url': valles_url
    }
    hemisphere_image_urls.append(valles)
    
#Cerberus Hemisphere
    
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Cerberus Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    cerberus_url = soup.find('div', class_ = 'downloads').a['href']
    cerberus_title = soup.find("h2", class_="title").text
    cerberus = {
        'title': cerberus_title,
        'img_url': cerberus_url
    }
    hemisphere_image_urls.append(cerberus)

#Schiaparelli Hemisphere

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = soup.find('div', class_= 'downloads').a['href']
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli = {
        'title': schiaparelli_title,
        'img_url': schiaparelli_url
    }   
    hemisphere_image_urls.append(schiaparelli)

#Syrtis Major Hemisphere
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    syrtis_url = soup.find('div', class_ = 'downloads').a['href']
    syrtis_title = soup.find("h2", class_='title').text
    syrtis= {
        'title': syrtis_title,
        'img_url': syrtis_url
    }
    hemisphere_image_urls.append(syrtis)

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_data
