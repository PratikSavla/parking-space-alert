from flask import Flask, render_template, request
from camera import Camera
import pyqrcode
import qr
import shakal

app = Flask(__name__)

@app.route('/')
def option():
	return render_template('option.html')


@app.route('/main.html')
def main():
   return render_template('main.html')

@app.route('/main2.html')
def main2():
   return render_template('main2.html')



@app.route('/result.html',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)



@app.route('/loc1.html')
def loc1():
	return render_template('loc1.html')

@app.route('/loc2.html')
def loc2():
	return render_template('loc2.html')

@app.route('/loc3.html')
def loc3():
	return render_template('loc3.html')
@app.route('/loc23.html')
def loc23():
	return render_template('loc23.html')
@app.route('/fail.html')
def fail():
	return render_template('fail.html')
@app.route('/admin.html')
def admin():
	return render_template('admin.html')

@app.route('/success.html')
def success():
	return render_template('success.html')

@app.route('/public.html')
def public():
	return render_template('public.html')

@app.route('/qr.html')
def qr1():
	shakal.TakeSnapshotAndSave()
	qr.generate_qr()
	return render_template('qr.html')




if __name__ == '__main__':
   app.run(debug = True)