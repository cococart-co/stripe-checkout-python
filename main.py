from flask import Flask, render_template
from util import get_checkout_session_url
app = Flask('app')

@app.route('/')
def checkout():
  url = get_checkout_session_url()
  return render_template("index.html", url=url)

app.run(host='0.0.0.0', port=8080)