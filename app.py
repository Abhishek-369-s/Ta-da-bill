from flask import Flask, render_template

app = Flask(__name__)

name='kothali'

@app.route("/")
def hello():
  return render_template('home.html',name=name)
 

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
