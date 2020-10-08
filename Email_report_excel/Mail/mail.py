import smtplib
from email.message import EmailMessage

import PySimpleGUI as Sg


# pop up com mensagem de erro
def pop_up(error):

    Sg.PopupOK("Error to send e-mail", error, title="ERROR", keep_on_top=True)


server_smtp = 'smtp.office365.com'
port_smtp = 587

USER = 'marcelocolige@hotmail.com'
PASSWORD = '1992Celao.'

msg = EmailMessage()

msg['From'] = USER
msg['To'] = 'mahcolige@gmail.com'
msg['Subject'] = f'Teste email python'

message = f"""This is a test e-mail message."""

msg.set_content(message)

try:
    server = smtplib.SMTP(server_smtp, port_smtp)
    server.starttls()
    server.login(USER, PASSWORD)
    server.send_message(msg)
    server.quit()
    print('enviado com sucesso')
except smtplib.SMTPAuthenticationError:
    pop_up("User authentication error.\nPlease, check username and password.")
except smtplib.SMTPException as exception:
    pop_up(exception)
