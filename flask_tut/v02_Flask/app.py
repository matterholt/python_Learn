from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisrationForm, LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = 'f3a37250268d0dddaf7db3f6480e08ff'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/Login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
