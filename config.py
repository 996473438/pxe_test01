class WebConfig:
    HOST = '192.168.1.30'
    PORT = 80


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    mysql_username = 'root'
    mysql_password = '123456'
    mysql_host = '192.168.1.30'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    database = 'test01'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(Config.mysql_username, Config.mysql_password,
                                                           Config.mysql_host, database)


class ProductionConfig(Config):
    database = 'product01'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(Config.mysql_username, Config.mysql_password,
                                                           Config.mysql_host, database)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
