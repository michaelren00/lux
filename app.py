from twilio.rest import Client
from flask import Flask, request
import json
import random

# from flask import Flask
app = Flask(__name__)

with open("LOGIN.txt") as file:
	login = file.readlines()

def getMessage():
	list_phrases = ["Have a good day!",
"Keep your head high!",
"Dreams turn into reality with the proper steps",
"You can do it!",
"You will always find a way!",
"You're doing great! Keep it up",
"Hope begins in the dark. Don't give up!",
"Get that bread!",
"Stay focused!",
"Believe in yourself, and you will succeed!",
"Life can be hard sometimes, but don't give up!",
"Even if you feel down, know that tomorrow will be a new day!",
"Always know that you are loved and cared by someone!",
"The struggle you’re in today is developing the strength you need tomorrow.",
"It’s not whether you get knocked down, it’s whether you get up.",
"Keep your face to the sunshine and you cannot see a shadow.",
"You’re braver than you believe, and stronger than you seem, and smarter than you think."]
	return list_phrases[random.randint(0,len(list_phrases))]
	
@app.route("/sendMessage", methods=["POST"])
def sendMessage():

	print(json.loads(request.data))
	data = dict(json.loads(request.data))

	account_sid = login[1]
	auth_token = login[3]
	client = Client(account_sid, auth_token)

	#returnSet = getMessage(previous)
	#previous = returnSet[0]

	message = client.messages \
	    .create(
	         body=getMessage(), 
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
