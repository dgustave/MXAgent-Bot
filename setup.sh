#!/bin/bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install wget 
brew install --cask anaconda 
python3 -m pip install --upgrade pip
pip install -U pyinstaller
brew install --cask chromedriver 
brew install --cask firefox

