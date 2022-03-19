#!/usr/bin/env python3

import speedtest
from datetime import datetime
import os
import smtplib
from email.message import EmailMessage
from segredo import senha #aqui vc importa um arquivo com a sua senha

class envia_email:

    def __init__(self):
        self._resultado = ''

    def net_verifica(self):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        # Testando velocidades
        velocidade_download = round(s.download(threads=None) * (10 ** -6))
        velocidade_upload = round(s.upload(threads=None) * (10 ** -6))
        # Capturando data e hora do teste
        data_atual = datetime.now().strftime('%d/%m/%Y')
        hora_atual = datetime.now().strftime('%H:%M')

        return f'Data:{data_atual}\nHora:{hora_atual}\nVelocidade Download:{velocidade_download}Mbps\nVelocidade Upload:{velocidade_upload}Mbps\n\n'

    def envia(self, mensagem):
        msgs = mensagem
    #configurando email e senha
        email_address = 'seu email vai aqui'
        email_password = senha

        #criar email
        msg = EmailMessage()
        msg['Subject'] = 'Relatório de velocidade da internet'
        msg['From'] = 'TI solution'
        msg['To'] = 'email do receptor'
        msg.set_content(msgs)

        #enviar email
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

        
email = envia_email()
email.envia(email.net_verifica())
