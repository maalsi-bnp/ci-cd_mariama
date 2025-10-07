# ci-cd_mariama


Template CI/CD pour TP4.


## Badges


![CI](https://github.com/<votre_utilisateur>/<nom_du_repo>/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/<votre_utilisateur>/<nom_du_repo>/actions/workflows/docker.yml/badge.svg)


## Structure


(voir arborescence dans le repo)


## Exécution locale


1. Installer dépendances : `pip install -r requirements.txt`
2. Lancer les tests : `pytest --cov=app`
3. Construire l'image Docker : `docker build -t ci-cd_votre_nom:local .`


## Publication GHCR


1. Créez un tag : `git tag v1.0.0 && git push --tags`
2. GitHub Actions buildera l'image et la publiera sur `ghcr.io/<votre_utilisateur>/<nom_du_repo>:v1.0.0`


## Déploiement


- Aller dans l'onglet Actions → `Deploy to production` → `Run workflow`.
- Le workflow utilise le secret `APP_SECRET` et cible l'environnement `production`.