from flask import Flask , render_template , request , redirect , url_for
from database import *

app = Flask(__name__)


@app.route('/')
def home():
	makeups = session.query(Makeup).all()
 	return render_template('home.html', makeups = makeups)

@app.route("/about_us")
def about_us():
 	return render_template("about_us.html")

@app.route("/makeup/<int:item_id>")
def makeup_item(item_id):
	item = session.query(Makeup).filter_by(id=item_id).one()
 	return render_template("makeup_item.html", item = item)


if __name__ == '__main__':
	app.run(debug=True)