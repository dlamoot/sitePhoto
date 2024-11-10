from flask import Flask, request, render_template

app = Flask(__name__)

# Page d'accueil avec le formulaire (si vous servez également le formulaire via Flask)
@app.route('/')
def index():
    return render_template('index.html')  # Assurez-vous que votre HTML est bien dans le dossier 'templates'

# Route pour traiter le formulaire
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Récupération des données du formulaire
    nom = request.form.get('nom')
    email = request.form.get('email')
    message = request.form.get('message')

    # Traitement ou stockage des données (ici on les affiche dans le terminal)
    print(f"Nom: {nom}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    # Réponse à l'utilisateur
    return "Merci pour votre message ! Nous vous contacterons sous peu."

# Exécuter l'application
if __name__ == '__main__':
    app.run(debug=True)
