"""
Toptal API
Unofficial Python API for Toptal (http://www.toptal.com/blog), including Toptal Blog and Toptal resume

$By Seth (Xiaohui) Wang
$email sethwang199418@gmail.com
"""

from constants import BASE, BLOG, SEARCH_BASE, topics
from utils import get_response, Soup
from bs4 import BeautifulSoup
import httplib2
import io, json, os, re

class Toptal(object):

    def __init__(self):
        self.BASE_URL = BASE
        self.SEARCH_BASE = SEARCH_BASE
        # self.http = httplib2.Http()

    def search(self, keyword, start, count):
        # construct search URL
        url = self.SEARCH_BASE + keyword + "&start=" + str(start) + "&count=" + str(count)
        # get http response
        response = get_response(url)
        # convert to json object
        json_res = json.loads(response)
        items = json_res["items"]

        result = []
        for item in items:
            i = Item(item["link"], item["title"])
            result.append(i)
            print i.title
            print i.url
        return result


    def trending(self):
        all_trending = []
        # get soup
        soup = Soup(self.BASE_URL + "/blog")

        for a in soup.find("nav", {"class" : "blog-trending"}).findAll("a"):
            # construct blog object
            i = Item(self.BASE_URL + a.get("href"), a.get_text())
            all_trending.append(i)

        return all_trending

    def newest(self):
        newest_posts = []

        url = self.BASE_URL + BLOG
        soup = Soup(url)
        a_tags = soup.find("div", {"class":"blog_posts-list"}).findAll("a")
        i = 0
        for a_tag in a_tags:
            url = self.BASE_URL + a_tag.get("href")
            title = a_tag.get_text()
            if i %10 == 1:
                item = Item(url, title)
                newest_posts.append(item)
            i += 1
        return newest_posts

    def topic(self, topic):
        if topic not in topics:
            return "Topic not Found"
        posts = []
        url = topics[topic]
        soup = Soup(url)
        a_tags = soup.find("div", {"class":"blog_posts-list"}).findAll("a")
        i = 0
        for a_tag in a_tags:
            url = self.BASE_URL + a_tag.get("href")
            title = a_tag.get_text()
            if i %10 == 1:
                item = Item(url, title)
                posts.append(item)
            i += 1
        return posts

class Item(object):
    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.content = ""
        self.type = ""

    def content(self, http):
        if self.content != "" and self.type == "blog":
            return self.content
        soup = Soup(self.url)
        # extract blog content
        self.content += soup.find("div", {"class":"content_body"}).get_text()
        return self.content

    def set_type(self, t):
        self.type = t

    def __str__(self):
        return self.title + "\n" + self.url + "\n"

class Freelencer(object):
    def __init__(self, url, name):
        self.name = name
        self.url = url
        self.tags = []

    def set_tags(tags):
        self.tags = tags

    def __str__(self):
        rep = self.name + "\n" + self.url + "\n"
        for tag in self.tags:
            rep += tag + " "
        return rep

if __name__ == "__main__":

    t = Toptal()
    #trending = t.trending()
    #print trending
    #print t.search("infrastructure", 11, 10)

    #for post in t.topic("backend"):
    #    print post
"""
    test extracting blog content
"""
    #b = Blog("https://www.toptal.com/remote/how-to-travel-and-work-full-time")
    #http = httplib2.Http()
    #b.content(http)
