from flask import Flask, render_template

app = Flask(__name__)

@app.route('/searchstuff', methods=['GET', 'POST'])
def main():
    return render_template('homepage.html')

@app.route('/showstuff', methods=['GET', 'POST'])
def shown():
    return render_template('suggested.html')
app.run(debug=True)
