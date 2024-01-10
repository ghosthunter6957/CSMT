import os, json
from flask import Flask, render_template, request, url_for, session, jsonify
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def main():
  return render_template('Index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  username = request.form.get('username')
  password = request.form.get('password')
  with open('data/passwords.json', 'r') as f:
    users = json.load(f)
  for user in users["users"]:
    if user["username"] == username and user["password"] == password:
      session['name'] = user["username"]
      session['passw'] = user["password"]
      if user["first"] == "Y":
        user["first"] = "N"
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
        return render_template('MainPage.html')
      else:
        return redirect(url_for('MainMenu'))
    elif user["username"] == username and user["password"] != password:
      return render_template('Index.html', Passerror="Invalid Password")
    f.close()
  return render_template('Index.html', Usererror="User not found")


@app.route('/Social', methods=['GET', 'POST'])
def Social():
  return render_template('/learning/Social.html')


@app.route('/MainMenu', methods=['GET', 'POST'])
def MainMenu():
  User = session.get('name')
  return render_template('MainMenu.html', username=User)


@app.route('/Phishing', methods=['GET', 'POST'])
def Phishing():
  return render_template('/learning/Phishing.html')


@app.route('/Passwords', methods=['GET', 'POST'])
def Passwords():
  print("hi")
  return render_template('/learning/Passwords.html')


@app.route('/InsiderThreats', methods=['GET', 'POST'])
def InsiderThreats():
  return render_template('/learning/InsiderThreats.html')


@app.route('/InsiderThreats2', methods=['GET', 'POST'])
def InsiderThreats2():
  return render_template('/learning/InsiderThreats2.html')


@app.route('/USB', methods=['GET', 'POST'])
def USB():
  return render_template('/learning/USB.html')


@app.route('/USB2', methods=['GET', 'POST'])
def USB2():
  return render_template('/learning/USB2.html')


@app.route('/USBQuiz', methods=['GET', 'POST'])
def USBQuiz():
  return render_template('/Quiz/USBQuiz.html')


@app.route('/PhishQuiz', methods=['GET', 'POST'])
def PhishQuiz():
  return render_template('/Quiz/PhishQuiz.html')


@app.route('/SocialQuiz', methods=['GET', 'POST'])
def SocialQuiz():
  return render_template('/Quiz/SocialQuiz.html')


@app.route('/PasswordQuiz', methods=['GET', 'POST'])
def PasswordQuiz():
  return render_template('/Quiz/PasswordQuiz.html')


@app.route('/InsiderThreatsQuiz', methods=['GET', 'POST'])
def InsiderThreatsQuiz():
  return render_template('/Quiz/InsiderThreatsQuiz.html')
  
@app.route('/Certificate', methods=['GET', 'POST'])
def Certificate():
  return render_template('Certificate.html')


@app.route('/Send_Data', methods=['GET', 'POST'])
def Send_Data():
  data = request.get_json()
  received_variable = list(data.keys())[0]  #key
  received_data = data.get(received_variable)  #value of key
  name1 = session['name']
  passw1 = session['passw']
  with open('data/passwords.json', 'r') as f:
    users = json.load(f)
  for user in users["users"]:
    if user["username"] == name1 and user["password"] == passw1:
      if received_variable == "passTotal":
        user["Pass"] = received_data
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
          f.close()
        return "InsiderThreats"
      elif received_variable == "phishTotal":
        user["Phish"] = received_data
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
          f.close()
        return "Passwords"
      elif received_variable == "usbTotal":
        user["USB"] = received_data
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
          f.close()
        return "Certificate"
      elif received_variable == "socialTotal":
        user["Social"] = received_data
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
          f.close()
        return "Phishing"
      elif received_variable == "insiderTotal":
        user["Insider"] = received_data
        with open('data/passwords.json', 'w') as f:
          json.dump(users, f)
          f.close()
        return "USB"
  return "Data Received"

@app.route('/Calculate', methods=['GET', 'POST'])
def Calculate():
  name1 = session['name']
  passw1 = session['passw']
  total_score = 0
  with open('data/passwords.json', 'r') as f:
    users = json.load(f)
  for user in users["users"]:
    if user["username"] == name1 and user["password"] == passw1:
      total_score = user["Pass"] + user["Phish"] + user["USB"] + user["Social"] + user["Insider"]
  return jsonify({'total_score': total_score})

app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
  app.run()
