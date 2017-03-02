from flask import Flask, render_template
app = Flask('server')


@app.route('/')
def webprint():
   return render_template('index.html')

if __name__ == '__main__':
#   Uncomment app.debug stuff to enable debug mode
#   app.debug = True
   app.run()
#   app.run(debug=True)
