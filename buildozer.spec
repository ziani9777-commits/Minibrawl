[app]

title = MiniBrawl
package.name = minibrawl
package.domain = org.minibrawl

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b

android.permissions = INTERNET,VIBRATE

android.archs = arm64-v8a, armeabi-v7a

android.presplash_color = #000000
android.bootstrap = sdl2

log_level = 2
