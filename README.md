#Toptal-API

Toptal-API is a python library to look up engineering blogs of various topics from [Toptal.com](http://toptal.com) (frontend, backend, database and etc).

## Setup
### Install with **pip**
```
  $pip install Toptal-API
```

### Install from source
```
  $ git clone git@github.com:wang502/Toptal-API.git
  $ cd Toptal-API
  $ python setup.py install
```

## Usage
### Use as command line interface
![screenshot](http://g.recordit.co/3VUDBBoN0V.gif)
- look up trending engineering blogs
```
  $ toptal --trending=true
  Trending engineering posts:
  1. The 10 Most Common Mistakes That Unity Developers Makeabout 13 hours ago
  http://toptal.com/unity-unity3d/top-unity-development-mistakes

  2. Productivity On The Road: Work Full-Time, Travel Solo, Have Fun4 days ago
  http://toptal.com/remote/how-to-travel-and-work-full-time

  3. Clustering Algorithms: From Start To State Of The Art4 days ago
  http://toptal.com/machine-learning/clustering-algorithms

  4. Toptal's Quick And Practical JavaScript Cheat Sheet: ES6 And Beyond6 days ago
  http://toptal.com/javascript/javascript-es6-cheat-sheet

  5. HTTP Request Testing: A Developer's Survival Tool18 days ago
  http://toptal.com/freelance/http-request-testing-a-survival-tool

  6. Express, Koa, Meteor, Sails.js: Four Frameworks Of The Apocalypse18 days ago
  http://toptal.com/nodejs/nodejs-frameworks-comparison

  7. Declarative Programming: Is It A Real Thing?20 days ago
  http://toptal.com/software/declarative-programming

  8. Using Scala.js With NPM And Browserify22 days ago
  http://toptal.com/scala/using-scala-js-with-npm-and-browserify
```
- Look up newest engineering blogs:
```
  $ toptal --newest=true
```
- search engineering blogs based on topic:
currently supported topic include: **frontend**, **backend**, **mobile**, **design**, **lifestyle**, **database**
```
  $ toptal --topic=backend
```
- search engineering blogs based on keyword:
```
  $ toptal --search=nodejs
```
### Use as library in your python script
```python
  import toptal
  t = Toptal()
  # search for blogs based on keyword, start from 1, search for 10 items
  posts1 = t.search('redis', 1, 10)
  # look up trending engineering blogs
  trendings = t.trending()
  # look up newest engineering blogs
  newests = t.newest()
  #
  posts2 = t.top('backend')
```
