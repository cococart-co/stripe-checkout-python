from flask import Flask
app = Flask('app')

stripeSecretKey = "sk_test_51IVvoGGpCUdxdLKw0LxioK1K3uR2b2tIZXIb3rP7tfotzdtPR7x5hINtPmm1EeIMdZpQRqu4SZgQsC30F62bsBPM00GZ97nIca"
subscriptionPriceId = "price_1IVvz3GpCUdxdLKwnHD5YcfO"

@app.route('/')
def checkout():
  return 'Stripe checkout'

app.run(host='0.0.0.0', port=8080)