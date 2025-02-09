from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pagina1.html')

@app.route('/pagina2', methods=['POST'])
def pagina2():
    username = request.form.get('username', '')  # Prende il nome utente dal form
    password = request.form.get('password', '')  # Prende la password dal form
    
    # Stampiamo i dati nel terminale
    print(f"🔹 Username: {username}")
    print(f"🔹 Password: {password}")
    
    return render_template('pagina2.html', username=username, password=password)

if __name__ == '__main__':
    print("✅ Flask sta partendo correttamente...")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
