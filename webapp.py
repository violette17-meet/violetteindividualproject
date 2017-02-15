from flask import Flask , render_template , request , redirect , url_for
from database import *

app = Flask(__name__)


@app.route('/')
def home():
 	return render_template('home.html')

@app.route("/about_us")
def about_us():
 	return render_template("about_us.html")

@app.route("/makeup/<item>")
def makeup_item(item):
 	return render_template("makeup_item.html", item = item)


if __name__ == '__main__':
	app.run(debug=True)