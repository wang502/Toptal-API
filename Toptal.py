"""
Toptal API
Unofficial Python API for Toptal (http://www.toptal.com/blog), including Toptal Blog and Toptal resume

$By Seth (Xiaohui) Wang
$email sethwang199418@gmail.com
"""

from constants import BASE, BLOG, SEARCH_BASE
from bs4 import BeautifulSoup
import httplib2
import io, json, os

class Toptal(object):

    def __init__(self):
        self.BASE_URL = BASE
        self.SEARCH_BASE = SEARCH_BASE
        self.http = httplib2.Http()

    def search_blog(self, keyword, count):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        # search from
        start = 1
        url = self.SEARCH_BASE + keyword + "&start=" + str(start) + "&count=" + str(count)
        status, response = self.http.request(url, 'GET', None, headers)
        json_res = json.loads(response)
        items = json_res["items"]

        result = []
        for item in items:
            b = Blog(item["formattedUrl"], item["title"])
            result.append(b)
        return result

    def trending(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        # http response
        status, response = self.http.request(self.BASE_URL + "/blog", 'GET', None, headers)
        soup = BeautifulSoup(response)
        blogs = []
        for a in soup.find("nav", {"class" : "blog-trending"}).findAll("a"):
            # construct blog object
            b = Blog(self.BASE_URL + a.get("href"), a.get_text())
            blogs.append(b)

        return blogs

class Blog(object):
    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.content = ""

    def content(self, http):
        if self.content != "":
            return self.content
        # browser header
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        tatus, response = http.request(self.url, 'GET', None, headers)
        soup = BeautifulSoup(response)
        # extract blog content
        self.content += soup.find("div", {"class":"content_body"}).get_text()
        return self.content

    def __str__(self):
        return self.title + "\n" + self.url

if __name__ == "__main__":

    t = Toptal()
    #trending = t.trending()
    #print trending
    #print t.search_blog("redis", 10)
"""
    test extracting blog content
"""
    #b = Blog("https://www.toptal.com/remote/how-to-travel-and-work-full-time")
    #http = httplib2.Http()
    #b.content(http)
