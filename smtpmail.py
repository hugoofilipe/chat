import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class mail():

  def envio(nome, email, _2fa):
      remetente = "dual@scorpionbonus.pt"
      destinatario = email

      corpo = "Mensagem enviado do DualChat\n\nUse o seu codigo 2AF:"+ _2fa + "\n\nBoas conversas!!!"

      correio = EmailMessage()
      correio.set_content(corpo)
      #correio = MIMEMultipart()
      correio['Subject']="Convite DualChat"
      correio['From']="DualChat, " + remetente
      correio['To']=nome +", " + destinatario

    #nomefich="extracao.csv"

    #with open(nomefich,"rb") as fich:
    #   part = MIMEApplication(fich.read(),Name=nomefich)
    #   part["Content-Disposition"] = 'attachment; filename="%s"' % nomefich
    #   correio.attach(part)

      try:
        smtpObj = smtplib.SMTP("mail.scorpionbonus.pt",587)
        smtpObj.starttls()
        smtpObj.login("dual@scorpionbonus.pt","Dual2023!")
        smtpObj.sendmail(remetente,destinatario,correio.as_string())
        smtpObj.close()
        print("Enviado com Sucesso!")
      except Exception as erro:
        print("Erro de envio:" + str(erro))

