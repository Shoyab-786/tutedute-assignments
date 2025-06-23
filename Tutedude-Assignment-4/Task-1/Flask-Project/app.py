from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

username = "Kalam"
password = "Kalam@963"  # your actual password here
password_encoded = quote_plus(password)

MONGO_URI = f"mongodb+srv://{username}:{password_encoded}@cluster1.r9jhnrd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(MONGO_URI)
db = client['mydatabase']
collection = db['submissions']

# rest of your Flask app code...

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            collection.insert_one({'name': name, 'email': email})
            return redirect('/success')
        except Exception as e:
            error = str(e)
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
