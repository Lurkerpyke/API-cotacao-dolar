import requests
import smtplib
import email.message


#pegar a informação que você quer
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

requisicao.dicionario = requisicao.json()
cotacao = float(requisicao.dicionario['USDBRL']['bid'])
print(cotacao)

#Envia e-mail automático


def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Cotação atual do dólar para real: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação do dólar atual"
    msg['From'] = 'exemplo.remetente@gmail.com' #remetente
    msg['To'] = 'exemplo.destinatario@gmail.com'#destinatário
    password = 'senha de aplicativo específico' #coloque sua senha de aplicativos específos aqui
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    s.quit()
   
        
        
if cotacao < 5.20:
    enviar_email(cotacao)
#deploy
