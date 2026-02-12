[app]
title = Mini Brawl Stars
package.name = minibrawl
package.domain = org.test
source.include_exts = py,png,jpg,wav,mp3,json
requirements = python3,kivy

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Install system packages
      run: |
        sudo apt update
        sudo apt install -y \
        build-essential git zip unzip openjdk-17-jdk \
        python3-pip autoconf libtool pkg-config \
        zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev

    - name: Install Python tools
      run: |
        python3 -m pip install --upgrade pip
        pip install buildozer cython

    - name: Install Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip
        unzip tools.zip
        mv cmdline-tools latest

        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH

    - name: Accept licenses & install SDK packages
      run: |
        yes | sdkmanager --licenses
        sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

    - name: Build APK
      run: |
        buildozer init || true
        buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apkname: Build APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Install system packages
      run: |
        sudo apt update
        sudo apt install -y \
        build-essential git zip unzip openjdk-17-jdk \
        python3-pip autoconf libtool pkg-config \
        zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev

    - name: Install Python tools
      run: |
        python3 -m pip install --upgrade pip
        pip install buildozer cython

    - name: Install Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip
        unzip tools.zip
        mv cmdline-tools latest

        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH

    - name: Accept licenses & install SDK packages
      run: |
        yes | sdkmanager --licenses
        sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

    - name: Build APK
      run: |
        buildozer init || true
        buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apkname: Build APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Install system packages
      run: |
        sudo apt update
        sudo apt install -y \
        build-essential git zip unzip openjdk-17-jdk \
        python3-pip autoconf libtool pkg-config \
        zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev

    - name: Install Python tools
      run: |
        python3 -m pip install --upgrade pip
        pip install buildozer cython

    - name: Install Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip
        unzip tools.zip
        mv cmdline-tools latest

        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH

    - name: Accept licenses & install SDK packages
      run: |
        yes | sdkmanager --licenses
        sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

    - name: Build APK
      run: |
        buildozer init || true
        buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apkname: Build APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Install system packages
      run: |
        sudo apt update
        sudo apt install -y \
        build-essential git zip unzip openjdk-17-jdk \
        python3-pip autoconf libtool pkg-config \
        zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev

    - name: Install Python tools
      run: |
        python3 -m pip install --upgrade pip
        pip install buildozer cython

    - name: Install Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip
        unzip tools.zip
        mv cmdline-tools latest

        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH

    - name: Accept licenses & install SDK packages
      run: |
        yes | sdkmanager --licenses
        sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

    - name: Build APK
      run: |
        buildozer init || true
        buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apk


orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.build_tools = 33.0.2
android.accept_sdk_license = True

[buildozer]
log_level = 2
