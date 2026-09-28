name: Build APK
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install System Dependencies
        run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk zip unzip python3-pip
          pip install --upgrade pip
          pip install buildozer cython==0.29.33

      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        id: buildozer
        with:
          command: buildozer android debug
          buildozer_version: stable

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: quiz-masti-apk
          path: bin/*.apk
