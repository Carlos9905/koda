import os
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple
from werkzeug.middleware.shared_data import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader, select_autoescape
import logging
from service.log import CustomFormatter

# Middleware personalizado para registrar solicitudes de archivos estáticos
class StaticFilesLoggerMiddleware:
    def __init__(self, app, static_files_path):
        self.app = app
        self.static_files_path = static_files_path
        self.logger = logging.getLogger('werkzeug')

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith(self.static_files_path):
            self.logger.info(f'Static file requested: {path}')
        return self.app(environ, start_response)

class Service:
    def __init__(self, config_file, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.config_file = config_file
        
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().handlers[0].setFormatter(CustomFormatter())

        # Configurar Jinja2
        templates_path = os.path.join(os.path.dirname(__file__), 'web', 'src', 'templates')
        self.jinja_env = Environment(
            loader=FileSystemLoader(templates_path),
            autoescape=select_autoescape(['html', 'xml'])
        )

        # Añadir middleware para servir archivos estáticos
        self.app = StaticFilesLoggerMiddleware(
            SharedDataMiddleware(self.application, {'/static': os.path.join(os.path.dirname(__file__), 'web', 'src')}),
            static_files_path='/static'
        )

        self.logger = logging.getLogger("KODA")

    def application(self, environ, start_response):
        try:
            # Aquí puedes agregar un enrutamiento más complejo si lo necesitas
            template = self.jinja_env.get_template('index.html')
            html_content = template.render()
            response = Response(html_content, mimetype='text/html')
        except Exception:
            response = Response('Page not found', status=404, mimetype='text/plain')
        return response(environ, start_response)

    def run(self):
        config_path = self.config_file if self.config_file else 'default'
        self.logger.info(f'Using configuration file: {config_path}')
        run_simple(hostname=self.host, port=self.port, application=self.app, use_reloader=True, use_debugger=True)

