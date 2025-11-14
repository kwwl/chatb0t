# 🤖 Chatbot Groq - Streamlit

Une interface utilisateur élégante pour interagir avec un chatbot basé sur **Groq** et alimenté par le modèle `gpt-oss-20b`.  
L’application utilise **Streamlit** pour le frontend et supporte le **streaming des réponses** en temps réel.

---

## 🎨 Fonctionnalités

- Interface **moderne et fluide** avec Streamlit.  
- Historique des messages conservé durant la session.  
- **Streaming en temps réel** des réponses du bot.  
- Séparation sécurisée de l’API key via `.env`.  
- Compatible macOS, Linux et Windows.

---

## ⚙️ Prérequis

- Python ≥ 3.10  
- pip  
- Accès à une **API key Groq**

---

## 📁 Structure du projet

chatb0t/
├─ app.py # Interface Streamlit
├─ main.py # Backend d’exemple avec Groq
├─ requirements.txt # Dépendances Python
├─ .env # Clé API (GROQ_API_KEY)
└─ chatbot_env/ # Environnement virtuel Python

yaml
Copier le code

---

## 🚀 Installation

1. **Créer et activer l’environnement virtuel :**  

```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate   # macOS / Linux
# ou sur Windows
chatbot_env\Scripts\activate
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Créer le fichier .env à la racine du projet :

Copier le code
GROQ_API_KEY=ta_clef_api_ici
🟢 Lancer l’application
bash
Copier le code
streamlit run app.py
Le chat s’ouvre automatiquement dans ton navigateur par défaut.

Tape ton message et clique sur Envoyer pour voir le bot répondre en temps réel.
