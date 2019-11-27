from flask import Flask, render_template, request
import pre_v1 as p
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# klo statis
@app.route('/setting')
def setting():
    return 'Halaman setting'

# klo dinamis
@app.route('/profile/<nama>')
def profil(nama):
    return render_template('template_dinamis.html', username=nama)
# klo dinamis
@app.route('/profile2/<int:id>')
def profil2(id):
    return f'Hello, ID kamu adalah {id}'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method== 'POST':
		query = request.form['email']
		hasil = p.cari(query)
		tmp =""
		for x in hasil:
			tmp += str(x) + ", "
		return render_template('hasil.html', index=hasil)
		# return '<h2>10 artikel terkait adalah artikel ke : ' + tmp+'</h2>'
	return render_template('login.html')