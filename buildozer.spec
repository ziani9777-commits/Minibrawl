[app]

title = Mini Brawl Stars
package.name = minibrawl
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,wav,mp3,json,kv

version = 1.0

requirements = 
python3,kivy==2.3.0,pillow,ffpyplayer

orientation = portrait
fullscreen = 0

# Android config
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license = True

android.permissions = INTERNET,VIBRATE

[buildozer]

log_level = 2
warn_on_root = 1
