import feedparser
import time

feed = feedparser.parse("https://www.heise.de/newsticker/heise-atom.xml")

tuples = [(entry.published_parsed, entry.title) for entry in feed.entries]
headlines = ["* [%s]: %s" % (time.strftime("%Y-%m-%d %H:%M:%S", pub_date), title) for pub_date, title in tuples]
[print(headline) for headline in headlines]