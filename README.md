# 🚀 FastAPI Detoxify API

Un projet FastAPI pour analyser la toxicité de commentaires texte avec le modèle **Detoxify** et stocker les résultats dans une base de données **MongoDB**.

---

## 📌 **Sommaire**

- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Lancer l'application en local](#lancer-lapplication-en-local)
- [Construire et exécuter avec Docker](#construire-et-exécuter-avec-docker)
- [Tester l'API](#tester-lapi)
- [Connexion à MongoDB](#connexion-à-mongodb)
- [Déployer sur GitHub](#déployer-sur-github)

---

## ⚙️ **Pré-requis**

- Python 3.10+
- Docker & Docker Compose
- Git
- Un compte GitHub avec **Personal Access Token (PAT)**

---

## 📦 **Installation**

```bash
# Cloner le projet (ou copier les fichiers)
git clone https://github.com/mouhib78/fastapi-detoxify.git
cd fastapi-detoxify

# Créer un environnement virtuel (facultatif mais recommandé)
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Télécharger les données NLTK nécessaires
python -m nltk.downloader stopwords

# Démarrer l'application avec Uvicorn
uvicorn fastapi_app:app --reload --host 0.0.0.0 --port 8090
# Construire l'image
sudo docker build -t fastapi-detoxify-app .

# Vérifier les images
sudo docker images

# Supprimer tout container existant avec le même nom (facultatif)
sudo docker rm -f fastapi-detoxify

# Exécuter le conteneur (mode host si besoin de MongoDB local)
sudo docker run -d --network host --name fastapi-detoxify fastapi-detoxify-app

# Voir les logs
sudo docker logs -f fastapi-detoxify


# Connexion à MongoDB
sudo systemctl status mongod
 
mongosh

show dbs
use toxic_comments
db.<nom_de_la_collection>.find().pretty()

