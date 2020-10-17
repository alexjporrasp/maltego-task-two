import configparser


config = configparser.ConfigParser()
config.read('prod.conf')

def crt_endpoint_url() -> str:
    return config.get('crt', 'endpoint_url')