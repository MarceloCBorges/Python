import PySimpleGUI as sg
from selenium import webdriver
import getpass

url = 'http://w2.samsung.net/'


def pede_senha():
    layout = [[sg.Text("Inform your password:", size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Samsung SDS Login', layout)
    event, values = window.read()
    window.close()
    if event == 'Submit':
        return values[0]
    if event == 'Cancel':
        quit()


sg.theme('Reddit')
password = pede_senha()

# abre navegador para manipulação
chrome = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver.exe")
chrome.get(url)

user = getpass.getuser()  # identifica usuário logado
# identificação e escrita campo usuário
user_input = chrome.find_element_by_id('USERID')
user_input.send_keys(user)
# identificação e escrita campo senha


password_input = chrome.find_element_by_id('USERPASSWORD')
password_input.send_keys(password)
sigIn_button = chrome.find_element_by_xpath("//button[@id='signIn']")
sigIn_button.click()
