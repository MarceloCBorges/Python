import PySimpleGUI as sg
import getpass

from selenium import webdriver

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


sg.theme('Reddit')
password = user_password()

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
