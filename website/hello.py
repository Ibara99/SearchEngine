from flask import Flask, render_template, request
import pre_v1 as p
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method== 'POST':
		query = request.form['email']
		hasil = p.cari(query)
		tmp =""
		for x in hasil:
			tmp += str(x) + ", "
		return render_template('hasil.html', index=hasil, query=query) 
		# return '<h2>10 artikel terkait adalah artikel ke : ' + tmp+'</h2>'
	return render_template('login.html')