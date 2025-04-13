from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def launch():
    return render_template('index.html')  # HTML launch page

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
