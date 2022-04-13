from flask import Flask, render_template
from util import getCheckoutSessionUrl
app = Flask('app')

@app.route('/')
def checkout():
  url = getCheckoutSessionUrl()
  return render_template("index.html", url=url)

app.run(host='0.0.0.0', port=8080)