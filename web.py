from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)  #debug=true means that you can update the code and it will update on the server real-time