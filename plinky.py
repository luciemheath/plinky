from flask import Flask
from flask import render_template, url_for, redirect
import logging
import yaml

app = Flask(__name__)

def load_shorturls():
  stream = open('./shorturls/shorturls.yaml')
  return yaml.load(stream)

def lookup_shorturl(shorturl):

@app.route("/", methods=['GET'])
@app.route("/<path:shorturl>", methods=['GET'])
def plinky(shorturl=None):
  if shorturl:
    app.logger.info('shorturl: %s' % shorturl)
    return "shorturl: %s" % shorturl
  else:
    return "the shorturl was missing"

@app.route("/discover", methods=['GET'])
def discover():
  return render_template('discover.html')

@app.route("/stats", methods=['GET'])
def stats():
  return  render_template('stats.html')

@app.route("/test", methods=['GET'])
def test():
  app.logger.error("this is an error")
  app.logger.warning("this is a warning")
  app.logger.info("this is info")
  app.logger.debug("this debug")

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
