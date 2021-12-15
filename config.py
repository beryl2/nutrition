import os
class Config:
    FOOD_API_BASE_URL = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}    
