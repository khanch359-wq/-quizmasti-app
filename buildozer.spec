[app]
title = Quiz Masti
package.name = quizmasti
package.domain = com.khanch359.quizmasti
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
[buildozer]
log_level = 2
[app:android]
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
