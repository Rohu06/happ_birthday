from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route to serve the birthday.html file
@app.route('/')
def birthday_page():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)