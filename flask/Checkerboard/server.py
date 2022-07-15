from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', height = 8, width = 8)
@app.route('/<int:height>')
def adjustHeight(height):
    return render_template('index.html', height = height, width = 8)
@app.route('/<int:height>/<int:width>')
def width_height(height, width):
    return render_template('index.html', height = height, width = width)
@app.route('/<int:height>/<int:width>/<color1>/<color2>')
def width_height(height, width, color1, color2):
    return render_template('index.html', height = height, width = width, color1 = color1, color2 = color2)
if __name__=="__main__":
    app.run(debug=True)
