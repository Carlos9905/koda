import click
import configparser
from pathlib import Path
from .config import Config

@click.command()
@click.option('--port', default=5000, type=int, help='Número de puerto para el servidor.')
@click.option('--config_file', type=click.Path(exists=True), help='Ruta del archivo de configuración.')
@click.option('--debug', is_flag=True, help='Activa el modo debug.')
@click.option('--test', is_flag=True, help='Activa los test.')
def main(port, config_file, debug, test):
    config = configparser.ConfigParser()
    if config_file:
        config.read(config_file)
        db_config = {k: v for k, v in config.items('Database')} if config.has_section('Database') else {}
        system_config = {k: v for k, v in config.items('System')} if config.has_section('System') else {}
    else:
        db_config = {}
        system_config = {}

    system_config['http_port'] = port if not system_config.get('http_port') else system_config['http_port']
    system_config['debug'] = debug if not system_config.get('debug') else system_config['debug']
    system_config['test'] = test if not system_config.get('test') else system_config['test']

    app_config = Config(db_config, system_config)
    print(app_config)
