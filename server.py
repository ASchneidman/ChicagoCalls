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
    return render_template('result_page.html', add = alderman)

if __name__ == '__main__':
    # Currently has debug stuff enabled
   app.debug = True
   app.run(debug=True)
