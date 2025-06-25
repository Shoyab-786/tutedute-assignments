from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/todo')  # 🔄 Redirect root to /todo

@app.route('/todo')
def todo_form():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)
