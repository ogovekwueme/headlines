import feedparser
from flask import Flask

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
    first_article = feed['entries'][0]
    return """<html>
      <body>
        <h1>Headlines</h1>
        <b>{0}</b><br />
        <i>{1}</i><br />

    
    <p>{2}</p><br />
      </body>
    </html>
    """.format(first_article.get('title'),
    first_article.get('date'),first_article.get('summary'))



if __name__ == '__main__':
    app.run(port=5000,debug=True)
