# Whatsapp-Filter

## Description
- Keeps a check on incoming messages.
- Filters out received messages according to pre-entered list of critical words/phrases.
- Separates messages having a match with critical words/phrases.
- Ease of getting useful information from piles of messages, rather than mining out important piece of texts from piles of conversations

## Dependencies
- Python version >= 3.6
- whatsapp-web library <br/>
  ```pip install whatsapp-web```
- selenium with geckodriver for firefox<br/>
  ```pip install selenium```<br/>
  ```pip install webdriver_manager```
- get geckodriver from https://github.com/mozilla/geckodriver/releases<br/>
  - extract ```sudo tar -xvf geckodriver-v0.26.0-linux64.tar.gz```
  - move Geckodriver to Binary location ``` sudo mv geckodriver /usr/local/bin/```
  - change cd to Binary ```cd /usr/local/bin/```
  - make executable permission to geckodriver ```sudo chmod +x geckodriver```
