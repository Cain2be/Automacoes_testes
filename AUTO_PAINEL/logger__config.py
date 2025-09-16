  
def log_config(suffix):
    """
    Função que redireciona todos os prints para um arquivo de log,
    mantendo as cores do terminal.
    """



    import sys
    import os
    from datetime import datetime

    class Logger:
        def __init__(self):
            # Garante que a pasta logs existe
            os.makedirs("logs", exist_ok=True)
            
            # Corrigindo a formatação do nome do arquivo
            log_filename = f"logs/{suffix}_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            
            self.terminal = sys.stdout
            self.log = open(log_filename, 'a', encoding='utf-8')
            self.closed = False

        def write(self, message):
            try:
                self.terminal.write(message)
                if not self.closed:
                    self.log.write(message)
            except ValueError:
                # Se o arquivo estiver fechado, continua apenas no terminal
                self.terminal.write(message)

        def flush(self):
            pass

        def close(self):
            if not self.closed:
                self.log.close()
                self.closed = True
                # Restaura o stdout padrão após fechar
                sys.stdout = self.terminal

    # Configuração automática
    sys.stdout = Logger()