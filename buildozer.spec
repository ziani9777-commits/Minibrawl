[app]

# (str) Titre de ton application
title = Brawl Stars Fan Game

# (str) Nom du package (sans espaces)
package.name = brawlstargame

# (str) Domaine du package (ex: org.test)
package.domain = org.votre.nom

# (str) Répertoire où se trouve le code source
source.dir = .

# (list) Extensions de fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Version de l'application
version = 0.1

# (list) Dépendances de l'application
# On ajoute 'kivy' car c'est ton moteur de jeu.
requirements = python3,kivy

# (str) Orientation de l'écran (portrait car ton code utilise 360x640)
orientation = portrait

# (bool) Indique si l'application doit être plein écran
fullscreen = 1

# (list) Permissions Android (Internet est souvent nécessaire)
android.permissions = INTERNET

# (int) API Android cible (33 est standard pour 2024/2025)
android.api = 33

# (int) API Android minimale
android.minapi = 21

# (str) Format de l'APK (debug pour tester, release pour le Play Store)
android.release_artifact = apk
android.debug_artifact = apk

# (list) Architectures supportées
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Niveau de log (2 est bien pour voir les erreurs)
log_level = 2

# (int) Avertir si on tourne en root
warn_on_root = 1
