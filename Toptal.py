"""
Toptal API
Unofficial Python API for Toptal (http://www.toptal.com/blog), including Toptal Blog and Toptal resume

$By Seth (Xiaohui) Wang
$email sethwang199418@gmail.com
"""

from constants import BASE, BLOG
from bs4 import BeautifulSoup
import httplib2
import io, json, os

class Toptal(object):

    def __init__(self):
        self.BASE_URL = BASE
        self.http = httplib2.Http()

    #def search_blog(self):


    def trending(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        status, response = self.http.request(self.BASE_URL + "/blog", 'GET', None, headers)
        soup = BeautifulSoup(response)
        for a in soup.find_all("a", {"class" : "blog-trending-item"}):
            print a

class Blog(object):


if __name__ == "__main__":

    t = Toptal()
    print t.trending()
