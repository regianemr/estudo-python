from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem 

    @abstractmethod
    def enviar (self) -> bool:... #avisando que é para retornar bool

class NotificacaoEmail(Notificacao):
     def enviar (self) -> bool:
         print('E-mail: enviando-', self.mensagem)
         return True

class NotificacaoSMS(Notificacao):
     def enviar (self)-> bool:
         print('SMS: Enviando-', self.mensagem)
         return False

# n = NotificacaoEmail ('Testando Notificação')
# n.enviar()
    
def notificar (notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print ('Notificação enviada')
    else:
        print('Notificação Não enviada')

notificacao_email = NotificacaoEmail('Testando')
notificar (notificacao_email)
notificacao_SMS= NotificacaoSMS ('Testando SMS')
notificar (notificacao_SMS)
