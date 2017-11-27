import feedparser
from flask import Flask, render_template

app = Flask(__name__)

rss_feeds = {'nba':'http://www.nba.com/rss/nba_rss.xml',
  'cnn':'http://rss.cnn.com/rss/edition.rss',
  'fox':'http://feeds.foxnews.com/foxnews/latest',
  'football':'http://feeds.feedburner.com/ChampionsLeagueFootballNews?format=xml'
}
@app.route('/')
@app.route("/<publication>")
def get_news(publication='nba'):
    feed = feedparser.parse(rss_feeds[publication])
    return render_template('index.html',
    articles = feed['entries'])





if __name__ == '__main__':
    app.run(port=5000,debug=True)
