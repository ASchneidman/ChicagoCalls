from flask import Flask, render_template, request, url_for, redirect
app = Flask('server')


@app.route('/')
def webprint():
   return render_template('index.html')

@app.route('/',methods = ['POST', 'GET'])
def alderman():
    if request.method == 'POST':
        alder = request.form["address"]
        return redirect(url_for('success',alderman = alder))
    else:
        alder = request.args.get("address")
        return redirect(url_for('success', alderman = alder))


@app.route('/success/<alderman>')
def success(alderman):
    return 'Your address is %s' % alderman

if __name__ == '__main__':
   app.debug = True
   app.run(debug=True)
