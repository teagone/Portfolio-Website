from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, template_folder='template')

JOBS = [
  {'id':1,
  'title': 'mister'}, 
  {'id':2,
    'title': 'misses'}, 
]
# url is made up of domain name and route
# homepage

@app.route("/")
def hello():
  return render_template("home.html", jobs =JOBS, CompanyName = 'Teagan')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)