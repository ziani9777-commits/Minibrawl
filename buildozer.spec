[app]

# Nom de ton jeu
title = MiniBrawl

# Nom du package (doit être unique)
package.name = minibrawl
package.domain = org.minibrawl

# Dossier contenant main.py
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav

# Version de l'app
version = 1.0

# Librairies python nécessaires
requirements = python3,kivy

# Orientation mobile
orientation = portrait

# Plein écran
fullscreen = 1

# Icône (optionnel)
# icon.filename = %(source.dir)s/icon.png

# Splash screen (optionnel)
# presplash.filename = %(source.dir)s/presplash.png


# ---------------- ANDROID ----------------

[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

# Versions compatibles Play Store
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b

# Permissions utiles
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Architecture CPU
android.archs = arm64-v8a, armeabi-v7a

# Empêche erreurs clavier Android
android.enable_androidx = True

# Empêche crash écran noir
android.allow_backup = False

# Mode plein écran immersif
android.fullscreen = True


# Optimisation build
p4a.branch = master
android.gradle_dependencies = androidx.core:core:1.9.0

# Empêche erreurs audio et fenêtre
android.presplash_color = #111111
android.window_translucent = False
