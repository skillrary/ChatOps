import os
from slackclient import SlackClient
from flask import Flask, request, Response


app = Flask(__name__)

#SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
#Don not share this key with anyone . it is copied from BOT user oauth token
SLACK_API_TOKEN = "n5Vw4snwTr8NNcoBDVZ0klbp"

#This sets the proxy to connect internet
#proxies = dict(https="https proxy uel with port number", http="https proxy with port number")

#This connects to the slack server if you are behind firewall then add one more param after api_token variable as proxies
slack_client = SlackClient(SLACK_API_TOKEN)


@app.route('/doit', methods=['POST'])
def inbound():
    print("inside inbound")
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200

@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    app.logger.debug("Request Headers %s", request)
    return None

#This function executes when you type trigger word along with the message you want to send it to your slackserver  eg. doit kkkkkk   doit is trigger word whcih needs to be configured in the outgoing webhooks
@app.route('/', methods=['GET','POST'])
def test():
    print("inside test")
    channel_id = request.form.get('channel_id')
    channel_name = request.form.get('channel_name')
    #This call sends the message
    slack_client.api_call( "chat.postMessage", channel=channel_id, text="*Hi How are you *")
    return Response('Hi Mithun!')


if __name__ == "__main__":
    app.run(debug=True)
