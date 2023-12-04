import logging

class CustomFormatter(logging.Formatter):
    """ Formateador de logging con colores para niveles específicos. """

    # Definición de colores usando códigos ANSI
    COLORS = {
        'WARNING': "\033[93m",   # Amarillo
        'INFO': "\033[92m",      # Verde
        'DEBUG': "\033[94m",     # Azul
        'CRITICAL': "\033[91m",  # Rojo
        'ERROR': "\033[91m",     # Rojo
        'RESET': "\033[0m"       # Reset
    }

    FORMAT = "%(asctime)s %(levelname)s: %(message)s"

    def __init__(self):
        super().__init__(fmt=self.FORMAT)

    def format(self, record):
        colored_levelname = f"{self.COLORS[record.levelname]}{record.levelname}{self.COLORS['RESET']}"
        record.levelname = colored_levelname
        return super().format(record)