class Enviador:
    def enviar(self, remetente, destinatario, assunto, mensagem):
        if '@' not in remetente:
            raise EmailInvalido(f'E-mail {remetente} inválido!')
        return remetente


class EmailInvalido(Exception):
    pass