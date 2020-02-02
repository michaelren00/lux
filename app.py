from twilio.rest import Client
from flask import Flask, request
import json

# from flask import Flask
app = Flask(__name__)

with open("LOGIN.txt") as file:
	login = file.readlines()


@app.route("/sendMessage", methods=["POST"])
def sendMessage():

	print(json.loads(request.data))
	data = dict(json.loads(request.data))

	account_sid = login[1]
	auth_token = login[3]
	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body='josh big smart',
	         from_=login[5],

	         #status_callback='http://postb.in/1234abcd',
	         to=str(data['to'])
	     )

	print(message.sid)
	return str(message.sid)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
