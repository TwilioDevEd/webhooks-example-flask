# Webhooks Example (Flask)

An example application that demonstrates how to build webhooks with Twilio and Flask, [visit this link](//www.local.twilio.com/docs/guides/webhooks/python#flask).

### Development

Getting your local environment setup to work with this app is ridiculously easy. 

1) Run the python flask file.
<pre>
python app.py
</pre>

2) Open browser to [http://localhost:5000/message](http://localhost:5000/message). Should see a message that this method is not allowed, since only Twilio can make requests to this url-- [see below](#twilio).

4) Tweak away on `app.py`.

### Webhook with Twilio {#twilio}

To learn how Twilio uses these webhooks to connect calls and messages [go here](//www.twilio.com/docs/guides/webhooks/python#flask).

## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.


[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/33a5ddd61dd29dd933422bca2b3dfa0e
"githalytics.com")](http://githalytics.com/TwilioDevEd/webhooks-example-flask)
