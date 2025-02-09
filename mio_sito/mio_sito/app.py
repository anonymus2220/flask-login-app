from flask import Flask, render_template, request

# Inizializza Flask e specifica la cartella dei template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('pagina1.html')  # Carica il file HTML correttamente

@app.route('/pagina2', methods=['POST'])
def pagina2():
    username = request.form.get('username', '')  # Prende il nome utente dal form
    password = request.form.get('password', '')  # Prende la password dal form
    return render_template('pagina2.html', username=username, password=password)

if __name__ == '__main__':
    print("✅ Flask sta partendo correttamente...")
    app.run(debug=True, port=5003)  # Usa la porta 5003
