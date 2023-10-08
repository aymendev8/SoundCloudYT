# SoundCloud to YouTube Video Uploader

Ce projet vous permet de télécharger des morceaux de musique depuis SoundCloud, de créer des vidéos à partir de ces morceaux en y ajoutant une image de couverture, et de téléverser automatiquement ces vidéos sur YouTube.

## Fonctionnalités

- Téléchargez des morceaux de musique depuis SoundCloud en spécifiant l'URL.
- Créez des vidéos à partir des morceaux téléchargés en ajoutant une image de couverture.
- Téléversez automatiquement les vidéos sur votre compte YouTube.

## Prérequis

- Python 3.x
- Bibliothèques Python : moviepy, sclib, google-api-python-client, oauth2client

## Configuration

1. Clonez ce dépôt GitHub.

git clone https://github.com/votre-utilisateur/soundcloud-to-youtube.git

2. Installez les bibliothèques Python requises en exécutant la commande suivante :

pip install moviepy sclib google-api-python-client oauth2client

3. Créez un projet sur la [Console de développement Google](https://console.developers.google.com/).

4. Activez l'API YouTube Data pour votre projet et configurez les identifiants OAuth 2.0.

5. Téléchargez le fichier JSON de clés d'API OAuth 2.0 depuis la Console de développement et nommez-le `client_secrets.json`. Placez ce fichier dans le même répertoire que votre script.

## Utilisation

1. Exécutez le script principal en utilisant la commande suivante :

python main.py

2. Saisissez l'URL SoundCloud du morceau que vous souhaitez télécharger et téléverser sur YouTube.

3. Cliquez sur le bouton "Upload to YouTube".

4. Le script téléchargera la musique depuis SoundCloud, créera une vidéo à partir de la musique et de l'image de couverture, puis la téléversera sur votre compte YouTube.

## Remarques

- Assurez-vous que le fichier `client_secrets.json` contient les informations d'identification correctes pour votre projet YouTube.

- N'oubliez pas de respecter les droits d'auteur et les conditions d'utilisation des morceaux de musique que vous téléchargez depuis SoundCloud.

## Licence

Ce projet est sous licence [MIT](LICENSE).
