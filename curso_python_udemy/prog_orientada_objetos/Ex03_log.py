from pathlib import Path  # Importa o módulo Path do pathlib para manipulação de caminhos de arquivos

# Define o caminho do arquivo de log, que será criado no mesmo diretório do script
LOG_FILE = Path(__file__).parent / 'log.txt'

# Classe base abstrata para logs
class Log:
    def _log(self, msg):
        # Método abstrato que deve ser implementado pelas subclasses
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')   
    

# Mixin para logar mensagens em um arquivo
class LogFileMixin(Log):
    def _log(self, msg):
        # Formata a mensagem para incluir o nome da classe
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        # Abre o arquivo de log no modo append (para adicionar ao final do arquivo)
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatada)  # Escreve a mensagem formatada no arquivo
            arquivo.write('\n')  # Adiciona uma nova linha após a mensagem
     

# Mixin para logar mensagens no console
class LogPrintMixin(Log):
    def _log(self, msg):
        # Imprime a mensagem no console, incluindo o nome da classe
        print(f'{msg} ({self.__class__.__name__})')       

# Bloco principal de execução do script
if __name__ == '__main__':
    lp = LogPrintMixin()  # Cria uma instância de LogPrintMixin
    lp.log_error('Qualquer coisa')  # Loga uma mensagem de erro
    lp.log_success('Que legal')  # Loga uma mensagem de sucesso
    lf = LogFileMixin()  # Cria uma instância de LogFileMixin
    lf.log_error('Qualquer coisa')  # Loga uma mensagem de erro em um arquivo
    lf.log_success('Que legal')  # Loga uma mensagem de sucesso em um arquivo


''' 
"Logar" é um termo técnico derivado do inglês "to log," que significa registrar ou 
escrever mensagens em um log, seja em um arquivo, console ou outro meio de armazenamento.

Um log é um registro de eventos, mensagens, ou outras informações que são coletadas
e armazenadas para análise futura.
'''