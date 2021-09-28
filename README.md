# Whatsapp-Filter

## Description
- Keeps a check on incoming messages.
- Filters out received messages according to pre-entered list of critical words/phrases.
- Separates messages having a match with critical words/phrases.
- Ease of getting useful information from piles of messages, rather than mining out important piece of texts from piles of conversations

## Dependencies
- Python version >= 3.6
- selenium with geckodriver for firefox<br/>
  ```pip install selenium```<br/>
  ```pip install webdriver_manager```
- get geckodriver from https://github.com/mozilla/geckodriver/releases<br/>
  - extract ```sudo tar -xvf geckodriver-v0.26.0-linux64.tar.gz```
  - move Geckodriver to Binary location ``` sudo mv geckodriver /usr/local/bin/```
  - change cd to Binary ```cd /usr/local/bin/```
  - make executable permission to geckodriver ```sudo chmod +x geckodriver```


## Getting started
* Fork this repository (Click the Fork button in the top right of this page, click your Profile Image)
* Clone your fork down to your local machine

```markdown
git clone https://github.com/your-username/Whatsapp-Filter.git
```

* Create a branch

```markdown
git checkout -b branch-name
```

* Make your changes
* Commit and push

```markdown
git add .
git commit -m 'Commit message'
git push origin branch-name
```

* Create a new pull request from your forked repository (Click the `New Pull Request` button located at the top of your repo)
* Wait for your PR review and merge approval!
* __Star this repository__ if you had fun!
