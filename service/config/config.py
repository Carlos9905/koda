from service.tools import Service

class Config:
    def __init__(self, db_config, system_config, config_file):
        self.db_name = db_config.get('db_name')
        self.db_port = db_config.get('db_port')
        self.db_host = db_config.get('db_host')
        self.db_user = db_config.get('db_user')
        self.db_pwd = db_config.get('db_pwd')
        self.http_port = system_config.get('http_port')
        self.debug = system_config.get('debug')
        self.test = system_config.get('test')
        self.host = system_config.get('host')
        self.config_file = config_file

    def __str__(self):
        return (f'Database Configuration:\n'
                f'  DB Name: {self.db_name}\n'
                f'  DB Port: {self.db_port}\n'
                f'  DB Host: {self.db_host}\n'
                f'  DB User: {self.db_user}\n'
                f'  DB Password: {self.db_pwd}\n'
                f'System Configuration:\n'
                f'  HTTP Port: {self.http_port}\n'
                f'  Debug: {self.debug}\n'
                f'  Test: {self.test})\n'
                f'  Host: {self.host}')
    
    def set_config(self):
        service = Service(config_file=self.config_file, host=self.host, port=self.http_port)
        service.run()