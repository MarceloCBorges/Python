import PySimpleGUI as sg
import getpass

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = 'http://w2.samsung.net/'


def user_password():
    layout_password = [[sg.Text("Inform your password:", size=(15, 1)), sg.InputText(password_char='*')],
                       [sg.Submit(), sg.Cancel()]]
    window_password = sg.Window('Samsung SDS Login', layout_password)
    event, values = window_password.read()

    if event == 'Submit':
        if values[0] == '':
            window_password.close()
            layout_error = [[sg.Text("Password cannot be blank.")], [sg.Ok()]]
            window_error = sg.Window('Error', layout_error)
            event = window_error.read()

            if event is not None:
                window_error.close()
                user_password()
            else:
                quit()
        else:
            return values[0]

    elif event == 'Cancel' or event is None:
        quit()


def login():
    global password

    user = getpass.getuser()  # identifica usuário logado
    # identificação e escrita campo usuário
    user_input = chrome.find_element_by_id('USERID')
    user_input.send_keys(user)
    # identificação e escrita campo senha

    password_input = chrome.find_element_by_id('USERPASSWORD')
    password_input.send_keys(password)
    sigin_button = chrome.find_element_by_xpath("//button[@id='signIn']")
    sigin_button.click()

    # msg senha incorreta
    try:
        if chrome.find_element_by_id("loginAlert"):
            alert_button = chrome.find_element_by_xpath("//button[@id='closeAlert']")
            alert_button.click()
            layout_alert = [[sg.Text("Incorrect Password.")], [sg.Ok()]]
            window_alert = sg.Window('Warning', layout_alert)
            event = window_alert.read()
            if event is not None:
                window_alert.close()
                password = user_password()
                login()
    except NoSuchElementException:
        pass


sg.theme('Reddit')
password = user_password()

# abre navegador para manipulação
chrome = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver.exe")
chrome.get(url)
login()
quit()
