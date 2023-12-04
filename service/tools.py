from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import logging
from service.log import CustomFormatter

class Service:

    def __init__(self, config_file,host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.config_file = config_file
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().handlers[0].setFormatter(CustomFormatter())

        # Configurar logging para Werkzeug a un nivel más alto que INFO
        logging.getLogger('werkzeug').setLevel(logging.WARNING)

        self.logger = logging.getLogger("KODA")

    def application(self, environ, start_response):
        request = Request(environ)
        response = Response('Hello World!', mimetype='text/plain')
        return response(environ, start_response)

    def run(self):
        self.logger.info(f'? Start KODA : http://{self.host}:{self.port}')
        config_path = self.config_file if self.config_file else 'default'
        self.logger.info(f'? Setting: {config_path}')
        self.logger.error('? ERROR')

        run_simple(hostname=self.host, port=self.port, application=self.application)

