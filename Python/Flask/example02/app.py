from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	led1State = GPIO.input(17)
	led2State = GPIO.input(18)
	if request.method == "POST":
		btnClicked = request.form.get("submitBtn")
		if int(btnClicked) == 1:
			nextState = not GPIO.input(17)
			led1State = nextState
			GPIO.output(17,nextState)
		elif int(btnClicked) == 2:
			nextState = not GPIO.input(18)
			led2State = nextState
			GPIO.output(18,nextState)
	return render_template("index.html", btn1State=int(led1State), btn2State=int(led2State))

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)
