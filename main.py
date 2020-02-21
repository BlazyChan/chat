from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('chat2.html')

@app.route('/chat')
def chat():
  return render_template('chat2.html')

@app.route('/chats/lasi')
def ielasit_chatu():
  chata_rindas = []
  with open("chats.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
  return jsonify({"chats": chata_rindas})


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  with open("chats.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["chats"] + "\n")

  return ielasit_chatu()
  
@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5001, threaded = True, debug = True)