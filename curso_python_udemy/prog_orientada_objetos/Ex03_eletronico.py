from Ex03_log import LogFileMixin  # Importa a classe LogFileMixin do módulo Ex03_log para registrar mensagens em um arquivo de log

# Classe base para dispositivos eletrônicos
class Eletronico:
    def __init__(self, nome):
        self._nome = nome  # Nome do dispositivo eletrônico
        self._ligado = False  # Estado inicial do dispositivo, desligado

    def ligar(self):
        # Método para ligar o dispositivo
        if not self._ligado:
            self._ligado = True  # Altera o estado para ligado

    def desligar(self):
        # Método para desligar o dispositivo
        if self._ligado:
            self._ligado = False  # Altera o estado para desligado

# Classe Smartphone que herda de Eletronico e LogFileMixin (herança múltipla)
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        # Chama o método ligar da classe base Eletronico
        super().ligar()

        # Verifica se o smartphone está ligado e registra a mensagem de sucesso no log
        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        # Chama o método desligar da classe base Eletronico
        super().desligar()

        # Verifica se o smartphone está desligado e registra a mensagem de erro no log
        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)


