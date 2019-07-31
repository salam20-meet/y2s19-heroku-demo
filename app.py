from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	food = ['pizza, mjadara, burger']
	return render_template("index.html", no_food=False,
	 food=food)

if __name__ == '__main__':
	app.run(debug = True)
