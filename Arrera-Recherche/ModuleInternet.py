import webbrowser
import requests

Navigateur =  "/usr/bin/firefox"
def TestInternet():
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        return True
    except requests.ConnectionError :
        return False

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.get(Navigateur).open(liengoogle)
def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.get(Navigateur).open(lienduck)
    
def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.get(Navigateur).open(lienQwant)

def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.get(Navigateur).open(lienEcosia)
  
def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.get(Navigateur).open(lienbing)
def LarousseSearch(query):
    with requests.session() as c:
        url = 'https://www.larousse.fr/dictionnaires/francais/'
        lienLarousse = url+query
        webbrowser.get(Navigateur).open(lienLarousse)
def WikipediaSearch(query):
    with requests.session() as c:
        url = 'https://fr.wikipedia.org/wiki/'
        lienWiki = url+query
        webbrowser.get(Navigateur).open(lienWiki)
def googleTrad(query):
    with requests.session() as c:
        url = 'https://translate.google.com/'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.get(Navigateur).open(liengoogle) 
def WordreferenceSearch(query):
    with requests.session() as c:
        url = 'https://www.wordreference.com/fren/'
        lienWord = url+query
        webbrowser.get(Navigateur).open(lienWord)

def YTmusicSearch(query):
    with requests.session() as c:
        url = 'https://music.youtube.com/search'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienYTmusic = urllink.url
        webbrowser.get(Navigateur).open(lienYTmusic)

def Mcarte():
    webbrowser.get(Navigateur).open("https://meteofrance.com/previsions-meteo-france/pas-de-calais/62")