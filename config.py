import os

class Config:
    '''
    General configuration parent class
    '''
    CATEGORY_URL='https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'
    SOURCE_URL='https://newsapi.org/v2/sources?language=en&country=us&apiKey={}'
    HEADLINE_URL ='https://newsapi.org/v2/top-headlines?language=en&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}