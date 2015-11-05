from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def incoming_call():
    """Twilio Voice URL - receives incoming calls from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    from_number = request.form['From']
    body = """
    Thanks for calling!

    Your phone number is {0}. I got your call because of Twilio's webhook.

    Goodbye!""".format(' '.join(from_number))
    resp.say(body)

    # Return the TwiML
    return str(resp)

@app.route('/message', methods=['POST'])
def incoming_message():
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Message> a text back to the person who texted us
    body = "Thanks for your text! My phone number is {0}. Webhooks are neat :)" \
        .format(request.form['To'])
    resp.message(body)

    # Return the TwiML
    return str(resp)

if __name__ == '__main__':
    app.run()
