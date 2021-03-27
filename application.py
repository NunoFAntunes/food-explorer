from flask import Flask, escape, request, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)