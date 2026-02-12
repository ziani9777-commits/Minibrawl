[app]

title = MiniBrawl
package.name = minibrawl
package.domain = org.minibrawl

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.permissions = INTERNET,VIBRATE

# ⚠️ ON BUILD APK (PAS AAB)
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
