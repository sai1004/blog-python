from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] =  'cffac5f6dca97f4164365db3b2cf6793'

posts = [

    {'author': 'sai',
     'title':'Blog post 1',
     'content':'First Blog Post',
     'country':'INDIA',
     'date_posted':'April 29, 2018'
     },
    {'author': 'sam',
     'title': 'Blog post 2',
     'content': 'Second Blog Post',
     'country': 'INDIA',
     'date_posted': 'April 5, 2018'
     },
    {'author': 'jake',
     'title': 'Blog post 3',
     'content':'Third Blog Post',
     'country': 'INDIA',
     'date_posted': 'April 2, 2018'
     },
]


@app.route('/')
@app.route('/home' ,methods=['GET'])
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def profile():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')