from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Counter"
@app.route('/')    
def count():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html', count = session["count"])

@app.route('/reset')
def reset():
    session["count"] = -1
    return redirect('/')

@app.route('/addTwo')
def plusTwo():
    session["count"] += 1
    return redirect('/')

@app.route('/destroysession')
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)