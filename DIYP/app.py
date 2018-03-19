import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flaskext.mysql import MySQL
from flask import request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

UPLOAD_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'tiff'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'DIYP'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM `Order`")
    data = cursor.fetchall()
    return render_template('index.html', test=data)


@app.route('/test', methods=['POST', 'GET'])


def test():
	if request.method == 'POST':
		Product = request.form.get('Product')
		Size = request.form.get('Size')
		Name = request.form['Name']
		Email = request.form['Email']
		ShippingAddress = request.form['ShippingAddress']
		file = request.files['file']
	        if file.filename == '':
	            flash('No selected file')
	            return redirect(request.url)
	        if file and allowed_file(file.filename):
	            filename = secure_filename(file.filename)
	            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	            file = (url_for('uploaded_file',filename=filename))
	            
		  

		cursor = mysql.get_db().cursor()
		sql = cursor.execute("INSERT INTO `Order` (`Product`,`Size`,`file`,`Name`, `Email`,`ShippingAddress`) VALUES ( %s,%s, %s,%s,%s,%s);", [Product,Size,file,Name,Email,ShippingAddress])
		mysql.get_db().commit()

		return redirect('Confirm')

	return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)



@app.route('/Confirm')
def Confirm():
	return render_template("Confirm.html")

if __name__ == "__main__":
 app.run(debug = True)