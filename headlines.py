import feedparser
from flask import Flask

app = Flask(__name__)

nba_feeds = 'http://www.nba.com/rss/nba_rss.xml'

@app.route("/")
def get_news():
    feed = feedparser.parse(nba_feeds)
    first_article = feed['entries'][0]
    return """<html>
      <body>
        <h1>NBA Headlines</h1>
        <b>{0}</b><br />
        <i>{1}</i><br />

    
    <p>{2}</p><br />
      </body>
    </html>
    """.format(first_article.get('title'),
    first_article.get('date'),first_article.get('title_detail')['value'])



if __name__ == '__main__':
    app.run(port=5000,debug=True)
