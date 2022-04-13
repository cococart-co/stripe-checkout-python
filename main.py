from flask import Flask
app = Flask('app')

@app.route('/')
def checkout():
  return 'Stripe checkout'

app.run(host='0.0.0.0', port=8080)