from flask import Flask
from twilio import twiml
app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def incoming_call():
    """Twilio Voice URL - receives incoming calls from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    resp.say("Thanks for calling! I got your call because of Twilio's webhook. Goodbye!")

    # Return the TwiML
    return str(resp)

@app.route('/message', methods=['POST'])
def incoming_message():
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    resp.message("Thanks for your text! Webhooks are neat :)")

    # Return the TwiML
    return str(resp)

if __name__ == '__main__':
    app.run()
