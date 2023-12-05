import requests
from bs4 import BeautifulSoup


#Defining the function that will get the text from the URl and find the required lyrics
def scraper(url):
    #Getting all information from the website
    web_response = requests.get(url)
    #Manipulating this raw data using bsoup
    web_soup = BeautifulSoup(web_response.content,'html5lib')
    lyrics = web_soup.find(id='songLyricsDiv')
    #Removing the stylizing left over from html scraping
    for word in lyrics.find_all('br'):
        word.replace_with('')
    print(lyrics)
    
#Defining the URL
song_url = 'https://www.songlyrics.com/kanye-west/jesus-walks-lyrics/'
scraper(song_url)
