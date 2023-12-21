import os, json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def main():
  return render_template('Index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  username = request.form.get('username')
  password = request.form.get('password')
  print("hello world")
  site_root = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(site_root, "data", "passwords.json")
  with open(json_url, 'r') as f:
    users = json.load(f)
  for user in users["users"]:
    if user["username"] == username and user["password"] == password:
      priv = user["privilege"]
      name = user["username"]
      return redirect(url_for('DashBoard', name=name, priv=priv))
    elif user["username"] == username and user["password"] != password:
      return render_template('Index.html', Passerror="Invalid Password")
  return render_template('Index.html', Usererror="User not found")


@app.route('/DashBoard', methods=['GET', 'POST'])
def DashBoard():
  name = request.args.get('name')
  priv = request.args.get('priv')
  return render_template('MainPage.html', name=name, priv=priv)


app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
  app.run()
