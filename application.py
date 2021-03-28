from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd7c19dbbe3940cf26b86e152ba7224cc5d0189e629690302939d33a8d13f6c72'

posts = [
	{
	'author': 'Nuno Antunes',
	'title': 'Sobre',
	'content': 'Este é o meu blog',
	'date_posted': '21 de Junho de 2020'
	},
	{
	'author': 'Admin',
	'title': 'Sobre',
	'content': 'Este era o meu blog',
	'date_posted': '22 de Junho de 2020'
	},
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for { form.username.data }!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title="Register", form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#Don't forget to remove this and make proper validation.
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash("You have been logged in!", "success")
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title="Register", form = form)


if __name__ == '__main__':
	app.run(debug=True)