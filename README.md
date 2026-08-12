# 🍋 Little Lemon — Restaurant Website (Django)

> Un site vitrine pour restaurant construit avec **Django** : menu dynamique piloté par base de données, panneau d'administration natif pour la gestion des plats, et interface responsive en CSS pur.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-07405E?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-blue)
![License](https://img.shields.io/badge/License-Not%20specified-lightgrey)

---

## 📖 Aperçu du projet

**Little Lemon** est une application web de démonstration développée avec Django, illustrant une architecture **MVT (Model-View-Template)** propre et idiomatique. Le projet répond à un besoin simple mais courant : offrir à un restaurant une vitrine web où le menu est géré dynamiquement depuis une base de données plutôt que codé en dur dans le HTML.

Il s'adresse principalement aux recruteurs techniques et développeurs souhaitant évaluer une implémentation Django claire (modèles, vues génériques basées sur les classes, gestion des médias, back-office admin) plutôt qu'une application de production à grande échelle.

## ✨ Fonctionnalités clés

- 🍽️ **Menu dynamique** — les plats (nom, prix, description, image) sont stockés en base et affichés via une `ListView` Django, avec tri alphabétique automatique.
- 🔍 **Pages de détail** — chaque plat dispose de sa propre page (`DetailView`) accessible depuis la grille du menu.
- 🖼️ **Gestion des images** — upload et affichage des photos de plats via `ImageField` et le système de fichiers médias de Django.
- 🛠️ **Panneau d'administration** — interface `django.contrib.admin` personnalisée (colonnes affichées, recherche par nom) pour ajouter/modifier/supprimer les plats sans toucher au code.
- 📄 **Pages statiques** — Accueil, À propos et Réservation (coordonnées du restaurant).
- 🎨 **UI responsive sur-mesure** — mise en page et style entièrement en CSS custom (pas de dépendance à un framework front-end lourd), avec une charte visuelle cohérente (header, hero, cartes menu, footer).
- 🧱 **Templates réutilisables** — héritage de templates Django (`base.html` + blocks) pour éviter la duplication de markup.

## 🏗️ Architecture & Stack technique

Le projet suit l'architecture **MVT** native de Django (équivalent du MVC côté serveur).

| Couche | Technologie | Rôle |
|---|---|---|
| **Backend** | Django 5 (Python) | Routing, logique métier, ORM |
| **Base de données** | SQLite | Stockage des plats du menu (adapté au contexte démo/dev) |
| **Templates** | Django Template Language | Rendu HTML côté serveur, héritage de templates |
| **Styles** | CSS custom (`static/styles.css`) | Mise en page responsive, sans framework CSS |
| **Médias** | `django.db.models.ImageField` + Pillow | Upload et service des images de plats |
| **Admin** | Django Admin | Back-office de gestion du menu |

**Structure applicative :**
- `littlelemon/` — configuration du projet (settings, routing racine, WSGI/ASGI)
- `restaurant/` — application métier (modèles, vues, admin, migrations)
- `Templates/` — templates HTML globaux
- `static/` — assets CSS
- `media/` — images uploadées (menu)

## 🚀 Guide d'installation & Démarrage rapide

### Prérequis
- Python 3.10+
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/ELGHAD/Restaurant-django.git
cd Restaurant-django

# 2. Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate      # Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install django pillow

# 4. Appliquer les migrations
python manage.py migrate

# 5. Créer un compte administrateur
python manage.py createsuperuser

# 6. Lancer le serveur de développement
python manage.py runserver
```

L'application est ensuite accessible sur `http://127.0.0.1:8000/`, et le back-office sur `http://127.0.0.1:8000/admin/`.

> ⚠️ Le dépôt ne contient pas de fichier `requirements.txt` : `django` et `pillow` (nécessaire pour `ImageField`) sont les dépendances minimales à installer manuellement.

## 📂 Structure du projet

```
Restaurant-django/
├── littlelemon/            # Configuration du projet Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── restaurant/              # Application principale
│   ├── models.py            # Modèle MenuItem
│   ├── views.py              # Vues fonction + génériques (List/Detail)
│   ├── admin.py               # Personnalisation de l'admin
│   ├── urls.py
│   └── migrations/
├── Templates/                # Templates HTML (base + pages)
│   └── restaurant/
├── static/                    # Fichiers CSS
├── media/menu_images/          # Images des plats uploadées
└── manage.py
```

## 🔐 Sécurité & bonnes pratiques

- **ORM Django** pour toutes les requêtes en base — protection native contre les injections SQL.
- **Middleware CSRF** activé par défaut sur les formulaires.
- **Accès admin restreint** aux comptes staff/superutilisateur via `django.contrib.admin`.
- **Vues génériques basées sur les classes** (`ListView`, `DetailView`) pour un code concis et testable.

**Points à adresser avant un déploiement en production** *(configuration actuelle héritée du mode développement)* :
- `SECRET_KEY` codée en dur et `DEBUG = True` dans `settings.py` — à externaliser via variables d'environnement.
- `ALLOWED_HOSTS` vide — à configurer pour l'hôte de production.
- SQLite convient au développement, mais une base plus robuste (PostgreSQL, par ex.) est recommandée en production.

## 🗺️ Pistes d'évolution

- Formulaire de réservation fonctionnel (actuellement une page informative statique).
- API REST (Django REST Framework) pour exposer le menu à un front-end découplé.
- Authentification utilisateur côté visiteur (comptes clients, historique de réservation).
- Tests unitaires (`restaurant/tests.py` est actuellement vide).

## 👤 Auteur & Contact

**Hamza Elrhadiouini**
Étudiant Ingénieur en Génie Logiciel (MIAGE) — EMSI Rabat

- 💻 GitHub : [@ELGHAD](https://github.com/ELGHAD)
- 🌐 Portfolio : [elghad.github.io/hamza-elrhadiouini-portfolio](https://elghad.github.io/hamza-elrhadiouini-portfolio)
- 📧 Email : [hamelrhadiouini@gmail.com](mailto:hamelrhadiouini@gmail.com)
