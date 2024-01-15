from flask import Flask , render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def show_counter():
    if "visits" not in session:
        session["visits"] = 1
    else:
        session['visits'] += 1
    return render_template('index.html')

@app.route('/', methods=['POST'])
def restart():
    session.pop('visits')# clears a specific key
    session['reset'] = request.form['reset']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)