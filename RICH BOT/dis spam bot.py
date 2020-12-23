import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test_driver = webdriver.Chrome('/Users/mukti/chromedriver')
test_driver.get('https://discord.com/channels/763021076283260958/775588110011596800')

time.sleep(3)

email = 'yourDiscordLoginGmail'
gmail = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
gmail.send_keys(email)


psw = 'yourdiscordPassword'
passs = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
passs.send_keys(psw)


login = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login.click()

time.sleep(30)

for i in range(0,999999):
        message = 'pls beg'
        message2 = 'pls dep max'
        text_box = test_driver.find_element_by_css_selector('#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div')
        text_box.send_keys(message)
        test_driver.find_element_by_css_selector("#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div").send_keys(Keys.RETURN)
        time.sleep(1)
        text_box = test_driver.find_element_by_css_selector('#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div')
        text_box.send_keys(message2)
        test_driver.find_element_by_css_selector("#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div").send_keys(Keys.RETURN)
        time.sleep(46)
        


