from bs4 import BeautifulSoup
import httplib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
http = httplib2.Http()

# get http response
def get_response(url):
    status, response = http.request(url, 'GET', None, headers)
    return response

# get soup
def Soup(url):
    response = get_response(url)
    return BeautifulSoup(response)
