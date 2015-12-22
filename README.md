# Webhooks Example (Flask)

An example application that demonstrates how to build webhooks with Twilio and Flask, [visit this link](//www.local.twilio.com/docs/guides/webhooks/python#flask).

## Installation

Step-by-step on how to deploy, configure and develop on this example app.

### Fastest Deploy

Use Heroku to deploy this app immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Getting Started 

1) Grab latest source
<pre>
git clone git://github.com/TwilioDevEd/webhooks-example-flask.git 
</pre>

2) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create
</pre>

3) Deploy to Heroku
<pre>
git push heroku master
</pre>

4) Scale your dynos
<pre>
heroku scale web=1
</pre>

5) Visit the home page of your new Heroku app to see your newly configured app!
<pre>
heroku open
</pre>

### Development

Getting your local environment setup to work with this app is similarly
easy.  After you configure your app with the steps above, use this guide to
get going locally:

1) Install the dependencies.
<pre>
make init
</pre>

2) Launch local development webserver
<pre>
foreman start
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `app.py`.

### Webhook with Twilio

To learn how Twilio uses these webhooks to connect calls and messages [go here](//www.twilio.com/docs/guides/webhooks/python#flask).

## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.


[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/33a5ddd61dd29dd933422bca2b3dfa0e
"githalytics.com")](http://githalytics.com/TwilioDevEd/webhooks-example-flask)