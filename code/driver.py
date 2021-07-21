from logging import log
import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriver

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage
from simon.pages import BasePage

driver = webdriver.Firefox()
driver.maximize_window()

# Login
login_page = LoginPage(driver)
login_page.load()
login_page.remember_me = False  #unchecking remember me
time.sleep(7)

# Base Page extends all pages 
    # Welcome page
    # nav bar page
    # search page
    # pane page
    # chat page // available only if a chat is open

base_page = BasePage(driver)
base_page.is_title_matches()

base_page.is_welcome_page_available()
base_page.is_nav_bar_page_available()
base_page.is_search_page_available()
base_page.is_pane_page_available()
base_page.is_chat_page_available()

# all open chats 
    # WONT work for contacts with no conversations
pane_page = PanePage(driver)

# getting chats
open_chats = pane_page.opened_chats

for oc in open_chats:
    print(oc.name)
    print(oc.last_message_time)
    print(oc.notifications)

first_chat = open_chats[0]
first_chat.click()

chat_page = ChatPage(driver)
msgs = chat_page.messages.unread()

for msg in msgs:
    print(msg.contact)
    print(msg.text)
    print(msg.date)

# Logging out
header_page = HeaderPage(driver)
header_page.logout()

# Closing the browser
driver.quit()