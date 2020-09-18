# importing necessary libraries
import os


from flask import (
    Flask,
    render_template,
    )

is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)