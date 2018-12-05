from flask import Flask, render_template, url_for

#
app = Flask(__name__)

# dummy post !list of dictonaries
posts = [
    {
        'author': "Matterholt",
        'title': "blog post",
        'content': " First post content",
        'date_posted': 'Dec, 01, 2018'
    },
    {
        'author': "Mr. Smith",
        'title': "blog post 2",
        'content': " Second post content",
        'date_posted': 'Dec, 02, 2018'
    }
]

# route decorators add addition features
# add route to file


@app.route('/')  # root folder
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title = 'aboutThis')


if __name__ == "__main__":
    app.run(debug=True)
