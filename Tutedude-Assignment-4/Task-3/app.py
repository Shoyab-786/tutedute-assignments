from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# ✅ MongoDB Atlas connection URI
client = MongoClient("mongodb+srv://Kalam:Kalam963@cluster1.r9jhnrd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")

# ✅ MongoDB DB & Collection setup
db = client.todo_db
collection = db.todo_items

@app.route('/')
def home():
    return redirect('/todo')

@app.route('/todo')
def todo_form():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        collection.insert_one({
            "name": item_name,
            "description": item_description
        })
        return "Item successfully submitted to MongoDB Atlas!"
    else:
        return "Missing item name or description", 400

if __name__ == '__main__':
    app.run(debug=True)
