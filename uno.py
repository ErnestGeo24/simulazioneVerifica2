from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # L'utente richiede la homepage
def tour():
  return render_template("tour.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)