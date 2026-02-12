[app]

title = MiniBrawl
package.name = minibrawl
package.domain = org.minibrawl

source.dir = .
source.include_exts = py,png,jpg,kv,mp3,wav,json

version = 1.0

requirements = python3,kivy==2.2.1,pillow

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

android.gradle_dependencies =

android.enable_androidx = True

android.logcat_filters = *:S python:D

p4a.branch = stable

log_level = 2
