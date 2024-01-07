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
  site_root = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(site_root, "data", "passwords.json")
  with open(json_url, 'r') as f:
    users = json.load(f)
  for user in users["users"]:
    if user["username"] == username and user["password"] == password:
      priv = user["privilege"]
      name = user["username"]
      if user["first"] == "Y":
        user["first"] = "N"
        with open(json_url, 'w') as f:
          json.dump(users, f)
        return redirect(url_for('DashBoard', name=name, priv=priv))
      else:
        return redirect(url_for('MainMenu', name=name, priv=priv))
    elif user["username"] == username and user["password"] != password:
      return render_template('Index.html', Passerror="Invalid Password") 
    f.close()
  return render_template('Index.html', Usererror="User not found")


@app.route('/DashBoard', methods=['GET', 'POST'])
def DashBoard():
  name = request.args.get('name')
  priv = request.args.get('priv')
  return render_template('MainPage.html', name=name, priv=priv)

@app.route('/MainMenu', methods=['GET', 'POST'])
def MainMenu():
  name = request.args.get('name')
  priv = request.args.get('priv')
  return render_template('MainMenu.html', name=name, priv=priv)

@app.route('/Social', methods=['GET', 'POST'])
def Social():
  return render_template('/learning/Social.html')

@app.route('/Phishing', methods=['GET', 'POST'])
def Phishing():
  return render_template('/learning/Phishing.html')

@app.route('/Passwords', methods=['GET', 'POST'])
def Passwords():
  return render_template('/learning/Passwords.html')

@app.route('/InsiderThreats', methods=['GET', 'POST'])
def InsiderThreats():
  return render_template('/learning/InsiderThreats.html')
  
@app.route('/USB', methods=['GET', 'POST'])
def USB():
  return render_template('/learning/USB.html')

@app.route('/PhishQuiz', methods=['GET', 'POST'])
def PhishQuiz():
  return render_template('/Quiz/PhishQuiz.html')

@app.route('/SocialQuiz', methods=['GET', 'POST'])
def SocialQuiz():
  return render_template('/Quiz/SocialQuiz.html')

@app.route('/PasswordQuiz', methods=['GET','POST'])
def PasswordQuiz():
  return render_template('/Quiz/PasswordQuiz.html')

app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
  app.run()
