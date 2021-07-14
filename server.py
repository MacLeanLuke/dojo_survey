from os import truncate
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():

    session['checkout'] = True

    print(request.form)

    session['first_name'] = request.form["first_name"]
    session['last_name'] = request.form["last_name"]
    session['email'] = request.form["email"]
    session['location'] = request.form["location"]
    session['language'] = request.form["language"]
    session['message'] = request.form["message"]

    return redirect('/results')

@app.route('/results')
def checkout_results():

    if 'checkout' not in session:
        return redirect('/')

    return render_template('checkout.html', first_name=session["first_name"],last_name=session["last_name"],email=session["email"],location=session["location"],language=session["language"],message=session["message"])

@app.route('/reset_click')
def reset_click():
    session.clear()
    session.modified = True
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True, port="5001")    